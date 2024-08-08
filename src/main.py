import logging.config
import etl_extraction, etl_transform
from modules.sources import extract_bees_brewery_api
from modules.sinks import save_local_folder
from modules.transformers import brewery_local

# Setup logging configuration
logging.config.fileConfig("./logging.conf")
logger = logging.getLogger(__name__)

def main():
    logger.info("Logging is working")

    # Extract
    fetch_func = extract_bees_brewery_api.get
    sink_func = save_local_folder.sink_to_local_folder

    info_bronze_data = etl_extraction.main(func_fetch=fetch_func, func_save=sink_func)
    print(info_bronze_data)

    bronze_path = info_bronze_data["full_path"]

    # Transform
    load_func = brewery_local.load_bronze_raw_data
    transf_func = brewery_local.transform_dataframe
    save_func = brewery_local.save_dataframe_as_parquet
    partition_column = brewery_local.get_column_partition_by()

    info_silver_data = etl_transform.main(bronze_path=bronze_path, load_func=load_func,
                                          transf_func=transf_func, save_func=save_func,
                                          partition_column=partition_column)

    
    print(info_silver_data)

if __name__ == "__main__":
    main()