import boto3
import logging.config
from datetime import datetime
from json import dumps
from botocore.exceptions import ClientError

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

S3_PATH = str(datetime.now().strftime("%Y%m%d%H%m%S"))
BUCKET_NAME = "bees-breweries-tf-bronze-bucket"
FILENAME = "data.json"


def sink_to_s3_bucket(bucket_name: str = BUCKET_NAME, filename: str = FILENAME,
                      data: object = None, s3_path: str = S3_PATH) -> dict:

    s3_key = f"{s3_path}/{filename}"

    tags = "Layer=Bronze&Project=Bees_Breweries"

    response_obj = {
        "save_successfull": False,
        "full_path": None,
        "size": 0
    }

    logger.debug(f"Attempting to create key {s3_key} in bucket {bucket_name}")

    # Initializing client
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=dumps(data),
                      ContentType="application/json", Tagging=tags)

        response_obj["save_successfull"] = True
        response_obj["full_path"] = f"{bucket_name}/{s3_key}"

        return response_obj

    except ClientError as e:
        logger.error(f"Client error while saving the data. : {e}")
        return response_obj
