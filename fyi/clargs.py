"""
Commandline arguments for verbosity.
"""
# TODO: include some logging to file stuff?


### IMPORTS

import string

import consts
import deflogger
import utils


### CONSTANTS & DEFINES

### CODE ###

def add_verbosity_argument (parser):
   parser.add_argument ("-v", "--verbosity",
      type=string.upper,
      choices=[
         'CRITICAL',
         'ERROR',
         'WARNING',
         'INFO',
         'DEBUG',
         'NOTSET',
         'NOTHING',
         'EVERYTHING',
      ],
      help="increase output verbosity"
   )

def set_versbosity_from_arg (arg, logger=None):
   if logger is None:
      logger = deflogger.get_default_logger()
   


### END #######################################################################

