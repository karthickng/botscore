""" Copyright @ karthickng@gmail.com.
Main entry point of the botscore program: handles command line processing.
"""

#! /usr/bin/env python

import sys
from twitterfeatures.twitterusers import TwitterUsers
from twitterfeatures.twitterfeatures import TwitterFeatures
from twitterlearn.checkbot import classify_complexity_metric
from error import UserListCreationError, UserTypeError
import os
from tests.dictionary import *

token= token_secret= consumer_key= consumer_secret= []

def _show_usage():
	""" Print usage help for program. """
	print("Usage: python3 main.py <API token> <token secret> <consumer key> <consumer secret>")
	sys.exit(1)
	
	'''print("Usage: botscore <userid>\n")
	sys.exit(0)
	'''
	
def process_cmd(args):
	""" Process command line arguments. """
	""".. todo:: Add more command line options """
	global token, token_secret, consumer_key, consumer_secret
	if len(args) != 5:
		_show_usage()
	
	#showusage() call above will quit if expected number of arguments not found
	#, so no check is made here		
	dummy, token, token_secret, consumer_key, consumer_secret = args
	
	return True

def test_twitterusers():
	global token, token_secret, consumer_key, consumer_secret
	t = TwitterUsers(token, token_secret, consumer_key, consumer_secret)
	t.read_user_list_json("data/userlist_train.json")
	#print("Test User list JSON:\n" + str(t.get_user_list()) + "\n")
	
	return t
	
def test_twitterfeatures(t):
	f = TwitterFeatures()
	f.extract_training_set_features(t)
		
if __name__ == "__main__":
	process_cmd(sys.argv)
	t = test_twitterusers()
	test_twitterfeatures(t)
	#print_dictionaries()
	#classify_complexity_metric(humanbow, botbow, t, "@vivekagnihotri")

#end of file
