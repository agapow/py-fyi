"""
Demonstrating the setting of verbosity on the commandline.
"""
# TODO: include some logging to file stuff?


### IMPORTS

import sys
import argparse

import fyi


### CONSTANTS & DEFINES

### CODE ###

if __name__ == '__main__':
   arg_parser = argparse.ArgumentParser()
   fy.add_verbosity_argument (arg_parser)
   clargs = sys.argv[1:]
   args = arg_parser.parse (clargs)
   



### END #######################################################################

