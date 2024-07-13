# This file is a part of FileStreamBot

from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig

import time

getLogger("aiohttp").setLevel(ERROR)
getLogger("pyrogram").setLevel(ERROR)
getLogger("aiohttp.web").setLevel(ERROR)

LOGGER = getLogger(__name__)


__version__ = "2.5.0"
StartTime = time.time()
