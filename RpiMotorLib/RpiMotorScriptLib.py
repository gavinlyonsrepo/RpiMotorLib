#!/usr/bin/env python3
"""
# ========================= HEADER =====================================
# title             :RpiMotorScriptlib.py
# description       :python placeholder  script to
# display the version and help for Rpi package RpiMotorlib
# author            :Gavin Lyons
# web               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.5.3
"""

# ==========================IMPORTS======================
# Import the system module needed to run rpiMotorScriptLib.py
import argparse
import sys

__version__ = "3.0-1"
__author__ = "Gavin Lyons"
__url__ = "https://github.com/gavinlyonsrepo/RpiMotorLib"

# ====================FUNCTION SECTION===============================


def process_cmd_arguments():
    """Function for processing command line arguments."""
    parser = argparse.ArgumentParser(description='RpiMotorLib : Raspberry Pi Motor Library \
     : A python 3 library for various motors and servos \
     to connect to a raspberry pi. \
     RpiMotorScript:Lib a script to display  \
    the version and help for rpiMotorlib.  \
    Written by ' + __author__ + '.  The project Documentation is at ' + __url__)
    parser.add_argument(
        '-v', help='Print rpiMotorlib version and quit',
        default=False, dest='version', action='store_true')

    args = parser.parse_args()
    return args


def main(args):
    """main function"""
    if len(sys.argv) == 1:
       print("usage: RpiMotorScriptLib.py [-h] [-v]")

    # display version
    if args.version:
        print("rpiMotorlib " + __version__)
        
    print("BYE")


# =====================MAIN===============================
if __name__ == "__main__":
    try:
        exit(main(process_cmd_arguments()))
    except (KeyboardInterrupt, SystemExit):
        pass

# =====================END===============================
