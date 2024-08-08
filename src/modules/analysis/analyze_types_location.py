import logging.config
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col

# # Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

INPUT_PATH = "data/silver/brewery.json"
OUTPUT_PATH = "data/gold/brewery_types_location.parquet"


def load_silver_raw_data(spark: SparkSession = None,
                         input_path: str = INPUT_PATH):
    try:
        df = spark.read.parquet(input_path)
        return df

    except Exception as e:
        print(f"Read operation failed: {e}")


def apply_business_logic(df):

    agg_df = df.groupBy(
        col("BreweryType"),
        col("StateProvince"),
    ).count()

    return agg_df


def save_dataframe_as_parquet(spark: SparkSession = None, df: DataFrame = None,
                              partition_by: str = "",
                              output_path: str = OUTPUT_PATH) -> dict:

    response_obj = {
        "save_successfull": False,
        "full_path": None,
        "size": 0
    }

    try:
        df.write.partitionBy(partition_by).mode("append").parquet(output_path)

        logger.debug(f"Saved file {output_path} successfully")

        response_obj["save_successfull"] = True
        response_obj["full_path"] = output_path

    except Exception as e:
        print(f"Write operation failed: {e}")

    return response_obj


def get_column_partition_by() -> str:
    return "StateProvince"
