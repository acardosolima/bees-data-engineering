import logging.config

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

def main():
    logger.info("Logging is working")
    return "main"

if __name__ == "__main__":
    main()