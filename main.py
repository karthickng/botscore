""" Copyright @ karthickng@gmail.com.
Main entry point of the botscore program: handles command line processing.
"""

#! /usr/bin/env python

import sys
from login import login, loginhelper


def processCmd(args):
	""" Process command line arguments. """
	
	for arg in args:
		print(arg)   # Print args

	
if __name__ == "__main__":
		processCmd(sys.argv)
		login()
		loginhelper()