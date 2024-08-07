import logging.config
from utils import get_full_function_name


# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

def load_bronze_raw_data(func):
    logger.debug(f"Loading bronze data using adapter "
                f"{get_full_function_name(func)}")

    df = func()

    return df

def save_dataframe_as_parquet(func, df: DataFrame = None):
    res = func(df)

    return res

from pyarrow import parquet as pq
import pyarrow as pa

# Define your input and output paths
input_path = 'path/to/local/input/file.json'
output_path = 'path/to/local/output/file.parquet'

# Read data from the input location
df = spark.read.option("multiline","true").json(input_path)

# Perform any necessary transformations
# Example: Select specific columns
df = df[["column1", "column2", "column3"]]

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Save the Table as a Parquet file to the output location
pq.write_table(table, output_path)

print(f"Data successfully saved as Parquet to {output_path}")
