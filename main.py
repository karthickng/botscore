""" Copyright @ karthickng@gmail.com.
Main entry point of the botscore program: handles command line processing.
"""

#! /usr/bin/env python

import sys
from TwitterFeatures.TwitterWrapper import TwitterWrapper
#from login import login, loginhelper

def show_usage():
	""" Print usage help for program. """
	
	print("Usage: botscore <userid>\n")
	sys.exit(0)
	
def process_user(userid):
	print(userid)
	TwitterWrapper(userid)
	pass

def process_cmd(args):
	""" Process command line arguments. """
	
	if len(args) != 2:
		show_usage()
		
	#showusage() call above will quit if expected number of arguments not found
	#, so no check is made here		
	t = TwitterWrapper(args)
	featuresList = t.getFeatures()
	print(featuresList)
		
	return True

	
if __name__ == "__main__":
		process_cmd(sys.argv)
		#login()
		#loginhelper()