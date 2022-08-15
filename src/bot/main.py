import logging
from os import getenv

from bot import main


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    main(getenv('token'))
