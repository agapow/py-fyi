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

def init_fyi():
	"""
	Do any necessary initialisation before calling fyi.
	"""
	pass


def init_default():
	"""
	The default handlers to set if none have been set when fyi is first called.

	You could question what happens if the programmer doesn't want *any*
	hanlders, but in that case:

	* they wouldn't even call fyi
	* they could always set the logging level to emit nothing

	"""
	pass

def get_logger (name=None):
	"""
	Return the named logger.
	"""
	return logging.getLogger (name)


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
