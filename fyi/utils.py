"""
Various utilities for manipulating logging and notifications.
"""

### IMPORTS

import sys
import logging
import types

import consts


### CONSTANTS & DEFINES

### CODE ###

def logger (name=None):
	"""
	Return the named logger.
	"""
	return logging.getLogger (name)


def set_level (level):
	logger().setLevel (level)


def config_level (level, hndlr_or_type=None, fmt=None):
	"""
	Tell the logger to how to handle a level.

	Note that this does assume that a logger will actually handle that level
	(i.e. log messages of that level), just what it will do if it does.
	See `handle_level` for that extra functionality.
	"""
	if isinstance (hndlr, logging.Handler):
		hndlr = hndlr_or_type
	else:
		hndlr = new_handler (hndlr_or_type=hndlr_or_type)

	hndlr.setLevel (level)
	fmtr = logging.Formatter (fmt)
	hndlr.setFormatter (fmtr)
	logger = logger()
	logger.addHandler (hndlr)


def handle_level (level, hndlr=None, fmt=None):
	"""
	Tell the logger to handle a level and optionally how to handle it.

	This tells a logger to log messages of a given level and how they will be
	logged. Note that if a logger is set up already for a different level,
	the more permissive level will be set.
	"""
	config_level (level, hndlr=hndlr, fmt=fmt)
	logger = logger()
	curr_level = logger.level
	if level < curr_level:
		logger.setLevel (level)


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

   
   
def to_level (v):
   """
   Transform a value into a level constant.

   This is intended largely to convert level names given as strings (e.g.
   'DEBUG') into the appropriate constant, but can also handle numbers. It
	also handles common typographical variations like case and flanking
	whitespace.
   """
   if isinstance (v, types.IntType):
      return v
   elif isinstance (v, basestring):
      v = v.upper().strip()
      lvl = consts.LEVEL_STR_MAP.get (v, None)
      if lvl is not None:
         return lvl
      else:
         try:
            lvl = int (v)
            return lvl
         except:
            raise exceptions.ValueError (
               "could not convert '%s' to fyi/logging level" % v
            )


### END #######################################################################

