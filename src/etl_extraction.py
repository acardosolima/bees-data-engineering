
import logging.config
import json
from utils import get_full_function_name
from modules.sources import extract_bees_brewery_api
from modules.sinks import save_aws_s3, save_local_folder

"""
This module provides methods to do Extraction steps.

Includes functions to fetch data from a source and sinking it into another 

"""

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

def fetch_data_from_api(func) -> json:
    """
    Executes a method to get data from a specific API

    Args:
        func: adapter method that fetches the API

    Returns:
        The json from the HTTP response
    """

    logger.debug(f"Request sent using adapter "
                f"{get_full_function_name(func)}")
    
    res = func()

    logger.debug(f"Request from {get_full_function_name(func)}"
                 f" return status {res.status_code}")

    if res.status_code== 200:
        return res.json()
    
def save_json_file(func, data: object = None) -> dict:
    """
    Executes a method to stores an object as json

    Args:
        func: adapter method that persists the object
        data: object to be persisted

    Returns:
        A dictionary with three attributes:
        - save_successfull: if operation is successfull
        - full_path: full path in filesystem where data is stored
        - size: file size in bytes
    """

    logger.debug(f"Trying to save using adapter "
                f"{get_full_function_name(func)}")

    res = func(data=data)

    if res["save_successfull"]:

        logger.debug(f"File saved in {res["full_path"]}, "
                        f"size: {res["size"]}")

        return res



def main(func_fetch, func_save) -> dict:

    # Calls the fetch data method using adapter received from main.py
    raw_data = fetch_data_from_api(func_fetch)

    # Calls the save json method using adapter received from main.py
    saving_resp = save_json_file(func_save, raw_data)

    return saving_resp