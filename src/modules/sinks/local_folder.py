import json
import os
import logging.config
from utils import validate_directory
from datetime import datetime

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

FILENAME = str(datetime.now().strftime("%Y%m%d%H%m%S")) + ".json"
PATH = "data/"

def sink_to_local_folder(filename: str = FILENAME, data: object = None,
                  path: str = PATH) -> dict:

    full_path = os.path.join(path,filename)

    validate_directory(path)

    response_obj = {
        "save_successfull": False,
        "full_path": None,
        "size": 0
    }

    logger.debug(f"Attempting to create file {full_path}")

    try:
        with open(full_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        response_obj["save_successfull"] = True
        response_obj["full_path"] = os.path.abspath(full_path)
        response_obj["size"] = os.path.getsize(full_path)

        return response_obj

    except PermissionError as e:
        logger.error(f"Permission denied while saving data. : {e}")
        return response_obj

    except OSError as e:
        logger.error(f"Error saving data. : {e}")
        return response_obj

if __name__ == "__main__":
    data = {"a": 1, "b": 2}

    print(sink_to_local_folder(data=data))
