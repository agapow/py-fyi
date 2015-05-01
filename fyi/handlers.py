"""
Setting and configuring handlers for various levels.

There's some confusing nomenclature here, so it's wise to define up front what
everything does:

set_level:
    Sets the level at which messages will be logged. Anything below this level
    will be ignored.

config_level:
    Describes the behaviour to occur at that particular level of logging.

handle_level:
    Describes the behaviour to occur at that particular level of logging and
    sets that level. Essentially a call to ``config_level`` followed by a call
    to ``set_level``.

new_handler:
    Create a handler (a destination), that can be used for logging at a
    particular level.

"""

### IMPORTS

import sys
import logging
import types

import consts


### CONSTANTS & DEFINES

### CODE ###

def set_level (level):
    """
    Set the level of message that will be displayed.

    Args:
        level: an fyi (or logging) level constant like INFO.

    """
	logging.logger().setLevel (level)


def config_level (level, hndlr_or_type=None, fmt=None):
	"""
	Tell the logger to how to handle a level.

    Args:
        level: an fyi (or logging) level constant like INFO.
        hndlr_or_type: see ``new_handler``
        fmt: see ``new_handler``

	Note that this does not assume that a logger *will* actually handle that
    level (i.e. log messages of that level), just what it will do if it does.
	See `handle_level` for that extra functionality.
	"""
	# if passed as actual handler, accept it, otherwise create from keyword
	if isinstance (hndlr_or_type, logging.Handler):
		hndlr = hndlr_or_type
	else:
		hndlr = new_handler (hndlr_or_type=hndlr_or_type)

	# associate handler with format and logger
	hndlr.setLevel (level)
	fmtr = logging.Formatter (fmt)
	hndlr.setFormatter (fmtr)
	root_logger = get_logger()
	root_logger.addHandler (hndlr)


def handle_level (level, hndlr_or_type=None, fmt=None):
	"""
	Tell the logger to handle a level and optionally how to handle it.

    Args:
        level: see ``config_level``
        hndlr_or_type: see ``new_handler``
        fmt: see ``new_handler``

	This tells a logger to log messages of a given level and how they will be
	logged. Note that if a logger is set up already for a different level,
	the more permissive / verbose level will be set.
	"""
	# configure level behaviour
	config_level (level, hndlr_or_type=hndlr_or_type, fmt=fmt)
	root_logger = get_logger()
	# set logger to use this level if it doesn't already
	curr_level = root_logger.level
	if level < curr_level:
		root_logger.setLevel (level)


def new_handler (hndlr_or_type=None, **kawrgs):
	"""
	Create a logging handler based on arguments.

	This allows us to create a
	"""
	## Preconditions & preparation:
	if hndlr_or_type is None:
		hndlr_or_type = consts.DEFAULT_HNDLR

	## Main:
	# if it's a handle, send output to there
	if hasattr (hndlr_or_type, 'write'):
		return logging.StreamHandler (hndlr_or_type)

	# if stdout or stderr is named, send it there
	if hndlr_or_type.upper() == 'STDOUT':
		return logging.StreamHandler (sys.stdout)
	if hndlr_or_type.upper() == 'STDERR':
		return logging.StreamHandler (sys.stderr)

	# if told 'file', look for path and mode args
	if hndlr_or_type.upper() == 'FILE':
		path = kwargs.get ('path', 'all.log')
		mode = kwargs.get ('mode', DEF_LOGGING_MODE)
		return logging.FileHandler (path, mode)

	# if a string, assume it is the name of a file
	if isinstance (hndlr_or_type, basicstring):
		mode = kwargs.get ('mode', DEF_LOGGING_MODE)
		return logging.FileHandler (path, mode)



### END #######################################################################
