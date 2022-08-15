import logging
from os import getenv
import bot

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    bot.main(getenv("TOKEN"))
