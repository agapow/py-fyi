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

def add_verbosity_arg (parser, short_flag='-v', long_flag='--verbosity'):
    """
    Configure a commandline parser to take a verbosity argument.

    Args:
        parser: an ``argparse`` commandline parser
        short_flag (str): the short commandline option, e.g. '-x'
        long_flag (str): the long commandline option, e.g. '--xxx'

    Example::

        clparser = argparse.ArgumentParser()
        add_verbosity_arg (clparser, '-n', '--noise')

    Commandline arguments should be logging levels (e.g. 'INFO'), although
    they can be written in any case.

    """
    # TODO: allow verbosity levels like 'NONE' or numerics. There's an issue
    # here in that lower numbers are more verbose, go figure.

    parser.add_argument (short_flag, long_flag,
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
      default='INFO',
      help="increase output verbosity"
   )

def set_verbosity_from_arg (arg, logger=None):
    """
    Taking a commandline argument, set the correct verbosity level.

    Args:
        arg (str): the level passed in on the commandline, e.g. 'INFO'
        logger: what logger to apply this to

    This work in conjunction with ``add_verbosity_arg`` to set the verbosity
    level from the commandline. In the future we should somehow allow this to
    describe logging to different loggers but not at the moment.

    """
    if logger is None:
      logger = deflogger.get_default_logger()
    level = utils.to_level (arg)
    logger.setLevel (level)



### END #######################################################################
