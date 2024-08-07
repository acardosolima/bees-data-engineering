import requests
import logging.config

# Setup logging configuration
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

URL = 'https://api.openbrewerydb.org/breweries'
HEADERS = {}

def get(url: str = URL, headers: dict = HEADERS) -> requests.Response:
        """
        Sends a GET request to an endpoint

        Args:
            url: endpoint to be accessed.
            headers: dictionary with request headers and their values.

        Returns:
            The requests.Response object with content, status code
            and response headers
        """
        res = requests.get(
            url=url,
            headers=headers)

        logger.debug(f"Request sent to {url} using "
                      f"({res.headers.get("Content-Type")}) returned"
                      f" status {res.status_code}")

        return res

def main():
        print(get(URL).json())

if __name__ == "__main__":
        main()