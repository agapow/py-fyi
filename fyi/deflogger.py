"""
Configuration of the default logger and notifications.

The default logger is the one used by fyi for the top-level module messaging
functions.

"""

### IMPORTS

import logging

import utils
import consts


### CONSTANTS & DEFINES

### CODE ###

def FyiLogger (logging.getLoggerClass()):
	def __init__ (self, name=None):
		builtin_logger_kls = logging.getLoggerClass()
		builtin_logger_kls.__init__ (self, name)



logging.setLoggerClass (FyiLogger)

def check_for_root_logger():
	"""
	Check if root logger has been initialised and if not, do so.
	"""
   if not (logging.root.handlers):
   	basicConfig()


def get_default_logger ():

	return utils.get_logger()


def set_default_logger (level=consts.DEFAULT_LEVEL, hndlr=None, fmt=None):
	def_logger = utils.get_logger()
	def_logger.setLevel (level)
	utils.config_level (level, hndlr, fmt)

set_default_logger()


def critical (msg):
	check_for_root_logger()
   get_default_logger().critical (msg)
   

def error (msg):
	check_for_root_logger()
	get_default_logger().error (msg)
   
   
def warning (msg):
	check_for_root_logger()
   get_default_logger().warning (msg)
   
   
def info (msg):
	check_for_root_logger()
   get_default_logger().info (msg)
   
   
def debug (msg):
	check_for_root_logger()
   get_default_logger().debug (msg)
   




### END #######################################################################

