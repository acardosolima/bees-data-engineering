# Use findspark library to setup pyspark 
import findspark
findspark.init()

import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder.appName("BreweryData").getOrCreate()

def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

schema = StructType([
    StructField("id", StringType(), False),
    StructField("name", StringType(), True),
    StructField("brewery_type", StringType(), True),
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

url = 'https://api.openbrewerydb.org/breweries'
data = fetch_data_from_api(url)

df = spark.createDataFrame(data, schema=schema)

df.show(5)

spark.stop()