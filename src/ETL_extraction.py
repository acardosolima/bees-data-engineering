
import logging.config
from utils import get_full_function_name
from modules.sources import bees_brewery_api
from modules.sinks import local_folder, aws_s3

"""
This module provides methods to do Extraction steps.

Includes functions to fetch data from a source and sinking it into another 

"""

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

def fetch_data_from_api(func):
    logger.debug(f"Request sent using adapter "
                f"{get_full_function_name(func)}")
    
    res = func()

    if res.status_code== 200:
        return res.json()
    
def save_json_file(func, data: object = None):
    logger.debug(f"Trying to save using adapter "
                f"{get_full_function_name(func)}")
    
    res = func(data=data)

    if res["save_successfull"]:
        logger.debug(f"File saved in {res["full_path"]}, "
                        f"size: {res["size"]}")
        
        return res



def main(func_fetch, func_save):

    raw_data = fetch_data_from_api(func_fetch)

    saving_resp = save_json_file(func_save, raw_data)

    return saving_resp