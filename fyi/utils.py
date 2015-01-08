"""
Various utilities for manipulating logging and notifications.
"""

### IMPORTS

import sys
import logging

import consts


### CONSTANTS & DEFINES

### CODE ###

def get_logger (name=None):
	return logging.getLogger (name)


def set_level (level):
	get_logger().setLevel (level)


def new_hndlr (hndlr_type=consts.DEFAULT_HNDLR, **kawrgs):
	"""
	Create a logging handler based on arguments.

	Serves to wrap around a lot of the 
	"""
	hndlr_type = hndlr_type.upper()
	if hndlr == 'STDOUT':
		return logging.StreamHandler (sys.stdout)
	if hndlr == 'STDERR':
		return logging.StreamHandler (sys.stderr)
	if hndlr == 'FILE':
		path = kwargs.get ('path', 'all.log')
		mode = kwargs.get ('mode', 'a')
		return logging.FileHandler (path, mode)


def config_level (level, hndlr=None, fmt=None):
	if hndlr is None:
		hndlr = logging.StreamHandler (sys.stdout)
	if fmt is None:
		fmt = consts.DEFAULT_FMT
	hndlr.setLevel (level)
	fmtr = logging.Formatter (fmt)
	hndlr.setFormatter (fmtr)
	logger = get_logger()
	logger.addHandler (hndlr)
   
   
def to_level (v):
   pass
   



### END #######################################################################

