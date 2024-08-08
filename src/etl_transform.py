import logging.config
from utils import get_full_function_name
from pyspark.sql import DataFrame, SparkSession

"""
This module provides methods to do Transform steps.

Includes functions to load data from bronze layer,
apply transformations and save dataset as parquet/delta

"""

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


def load_bronze_raw_data(func, spark: SparkSession,
                         input_path: str) -> DataFrame:
    """
    Executes a method to gather the bronze data

    Args:
        func: adapter method that fetches the raw file
        spark: spark sesssion to be used in the operation
        input_path: location of data file

    Returns:
        Dataframe of bronze file
    """

    logger.debug(f"Loading bronze data using adapter "
                 f"{get_full_function_name(func)}")

    df = func(spark=spark, input_path=input_path)

    return df


def transform_dataframe(func, df: DataFrame) -> DataFrame:
    """
    Executes a method to execute transformations in provided dataframe

    Args:
        func: adapter method that transforms the dataframe
        df: dataframe to be worked on

    Returns:
        Dataframe with all required transformations
    """

    logger.debug(f"Transforming dataframe using adapter "
                 f"{get_full_function_name(func)}")

    df = func(df)

    return df


def save_dataframe_as_parquet(func, spark: SparkSession, df: DataFrame,
                              partition_by: str, output_path: str):
    """
    Executes a method to persist dataframe to silver layer

    Args:
        func: adapter method that sinks the data in silver layer
        spark: spark sesssion to be used in the operation
        df: dataframe to be saved
        output_path: location of the dataframe in silver layer

    Returns:
        A dictionary with three attributes:
        - save_successfull: if operation is successfull
        - full_path: full path in filesystem where data is stored
        - size: file size in bytes
    """

    logger.debug(f"Saving dataframe as parquet using adapter "
                 f"{get_full_function_name(func)}")

    res = func(spark=spark, df=df, partition_by=partition_by,
               output_path=output_path)

    return res


def main(bronze_path: str, load_func, transf_func,
         save_func, partition_column) -> dict:

    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("BeesBreweries") \
        .getOrCreate()

    # Path to store the transformed dataframe in silver layer
    silver_path = bronze_path.replace("bronze", "silver") \
        .replace(".json", ".parquet")

    # Calls the load bronze method using adapter received from main.py
    raw_df = load_bronze_raw_data(load_func, spark=spark,
                                  input_path=bronze_path)

    # Calls the transform data method using adapter received from main.py
    transf_df = transform_dataframe(transf_func, raw_df)

    # Calls the save as parquet method using adapter received from main.py
    res = save_dataframe_as_parquet(save_func, spark=spark,
                                    df=transf_df,
                                    partition_by=partition_column,
                                    output_path=silver_path)

    return res
