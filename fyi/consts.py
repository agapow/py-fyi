"""
Module wide constants.

The levels are simply copied from the logging module. They are actually just
integer values, where the higher the less information you see (and the
only information you see is more and more important):

* CRITICAL 50
* ERROR 40
* WARNING  30
* INFO  20
* DEBUG 10
* NOTSET   0

"""

### IMPORTS

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET


### CONSTANTS & DEFINES

INITED = False

NOTHING = 100
EVERYTHING = 1

LEVELS = (CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET, NOTHING, EVERYTHING)

DUMP = DEBUG

LEVEL_STR_MAP = {
   'CRITICAL': CRITICAL,
   'ERROR': ERROR,
   'WARNING': WARNING,
   'INFO': INFO,
   'DEBUG': DEBUG,
   'NOTHING': NOTHING,
   'EVERYTHING': EVERYTHING,
}

DEFAULT_LEVEL = INFO

DEFAULT_HNDLR = 'STDOUT'

DEFAULT_FMT = '%(levelname)s: %(message)s'
DEFAULT_CRITICAL_FMT = DEFAULT_FMT
DEFAULT_ERROR_FMT = DEFAULT_FMT
DEFAULT_WARNING_FMT = DEFAULT_FMT
DEFAULT_INFO_FMT = DEFAULT_FMT
DEFAULT_DEBUG_FMT = DEFAULT_FMT


### END #######################################################################
