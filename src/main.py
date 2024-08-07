import etl_extraction
import logging.config
from modules.sources import bees_brewery_api
from modules.sinks import local_folder


# Setup logging configuration
logging.config.fileConfig("./logging.conf")
logger = logging.getLogger(__name__)

def main():
    logger.info("Logging is working")

    fetch_func = bees_brewery_api.get
    sink_func = local_folder.sink_to_local_folder

    info_raw_data = etl_extraction.main(fetch_func, sink_func)
    print(info_raw_data)

    location = info_raw_data["full_path"]


    return "main"

if __name__ == "__main__":
    main()