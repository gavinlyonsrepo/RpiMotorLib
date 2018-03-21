#!/usr/bin/env python3
"""python script to display the version and help for rpiMotorlib"""
# =========================HEADER=======================================
# title             :RpiMotorScriptlib.py
# description       :python placeholder  script to
# display the version and help for RpiMotorlib
# author            :Gavin Lyons
# date              :15/03/2018
# version           :1.0-1
# web               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.6.0

# ==========================IMPORTS======================
# Import the system module needed to run rpiMotorScriptLib.py
import argparse
import sys

__version__ = "1.0-1"
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
    Written by ' + __author__ + '.  Readme at Url ' + __url__)
    parser.add_argument(
        '-v', help='Print rpiMotorlib version and quit',
        default=False, dest='version', action='store_true')

    args = parser.parse_args()

    # if len(sys.argv) == 1:
    #    print("usage: RpiMotorScirptLib.py [-h] [-v]")

    # display version
    if args.version:
        print("rpiMotorlib " + __version__)

    return args


def main(args):
    """main function"""
    pass


# =====================MAIN===============================
if __name__ == "__main__":
    try:
        exit(main(process_cmd_arguments()))
    except (KeyboardInterrupt, SystemExit):
        pass

# =====================END===============================
