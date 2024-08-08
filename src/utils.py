import logging.config
from pathlib import Path


"""
This module provides various utils functions to be used by other modules.

"""

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


def get_full_function_name(func) -> str:
    """
    Gets full method name

    Args:
        func: function instance

    Returns:
        Name in format <module>.<method>
    """
    module_name = func.__module__
    function_name = func.__name__

    return f"{module_name}.{function_name}"


def validate_directory(path: str) -> bool:
    """
    Validates a given directory

    Args:
        path: directory to be checked

    Returns:
        True if method created directory or it already exists
        False otherwise
    """
    directory = Path(path)

    try:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Directory created in {directory}")
        else:
            logger.debug(f"Directory {directory} already exists")

        return True

    except PermissionError as e:
        logger.error(f"Permission denied trying create directory: {e}")
    except OSError as e:
        logger.error(f"Error accessing file system: {e}")


def snake_to_pascal(snake_str):
    """
    Converts a snake_case string to PascalCase.

    Args:
        snake_str (str): string in snake_case

    Returns:
        string in PascalCase
    """
    return ''.join(word.capitalize() for word in snake_str.split('_'))
