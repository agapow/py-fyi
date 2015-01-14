"""
Configuration of the default logger and notifications.

The default logger is the one used by fyi for the top-level module messaging
functions.

"""

### IMPORTS

import utils
import consts


### CONSTANTS & DEFINES

### CODE ###

def get_default_logger ():
	return utils.get_logger()


def set_default_logger (level=consts.DEFAULT_LEVEL, hndlr=None, fmt=None):
	def_logger = utils.get_logger()
	def_logger.setLevel (level)
	utils.config_level (level, hndlr, fmt)

set_default_logger()


def critical (msg):
   get_default_logger().critical (msg)
   

def error (msg):
   get_default_logger().error (msg)
   
   
def warning (msg):
   get_default_logger().warning (msg)
   
   
def info (msg):
   get_default_logger().info (msg)
   
   
def debug (msg):
   get_default_logger().debug (msg)
   




### END #######################################################################

