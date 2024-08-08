from pyspark.sql.types import StructField, StructType, StringType


def get_brewery_schema() -> StructType:
    """
    Returns the schema for OpenBrewery API data

    Args:

    Returns:
        Pyspark StructType with columns metadata
    """

    df_schema = StructType([
        StructField("id", StringType(), False),
        StructField("name", StringType(), False),
        StructField("brewery_type", StringType(), False),
        StructField("address_1", StringType(), True),
        StructField("address_2", StringType(), True),
        StructField("address_3", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state_province", StringType(), True),
        StructField("postal_code", StringType(), True),
        StructField("country", StringType(), True),
        StructField("longitude", StringType(), True),
        StructField("latitude", StringType(), True),
        StructField("phone", StringType(), True),
        StructField("website_url", StringType(), True),
        StructField("state", StringType(), True),
        StructField("street", StringType(), True)
    ])

    return df_schema
