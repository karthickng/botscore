""" Copyright @ karthickng@gmail.com.
Main entry point of the botscore program: handles command line processing.
"""

#! /usr/bin/env python

import sys
from TwitterFeatures.TwitterWrapper import TwitterWrapper
#from login import login, loginhelper

def showUsage():
	""" Print usage help for program. """
	
	print("Usage: botscore <userid>\n")
	sys.exit(0)
	
def processUser(userid):
	print(userid)
	TwitterWrapper(userid)
	pass

def processCmd(args):
	""" Process command line arguments. """
	
	if len(args) != 2:
		showUsage()
		
	#showusage() call above will quit if expected number of arguments not found
	#, so no check is made here		
	t = TwitterWrapper(args)
	featuresList = t.getFeatures()
	print(featuresList)
		
	return True

	
if __name__ == "__main__":
		processCmd(sys.argv)
		#login()
		#loginhelper()