""" Package-level data """

from fpkmfetcher.fpkmfetcher import *
from fpkmfetcher.processing import *

import logmuse
import coloredlogs

_LOGGER = logmuse.init_logger("fpkmfetcher")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)
