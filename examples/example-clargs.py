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
   ap = argparse.ArgumentParser()
   fyi.add_verbosity_argument (ap)
   clargs = sys.argv[1:]
   args = ap.parse_args (clargs)
   fyi.set_versbosity_from_arg (args.verbosity)
   
   fyi.critical ('a message')
   fyi.error ('a message')
   fyi.warning ('a message')
   fyi.info ('a message')
   fyi.debug ('a message')
   


### END #######################################################################

