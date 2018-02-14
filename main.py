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

""".. todo:: take from command line or file """
""".. todo:: delete token after development """
token = "3018287190-tG4K1NW1OAUMKi1IhKsFn41LwBsnSsYfj0GA6vX"
token_secret = "7zivxHb2ckKEnY3TlWojjLr6Rpcxh5ikQyvGdgaJhAlU8"
consumer_key = "BXrC55ZUlvmuuGeLnzIqW4nhr"
consumer_secret = "Tit9mp5hwG9CbDrOMDywTNKghVOzDQ9wqhCAFKGW8LLBt7IXAt"

def _show_usage():
	""" Print usage help for program. """
	
	print("Usage: python3 main.py <userid>")
	sys.exit(0)
	
	'''print("Usage: botscore <userid>\n")
	sys.exit(0)
	'''
	
def process_cmd(args):
	""" Process command line arguments. """
	""".. todo:: Add more command line options """
	
	if len(args) != 2:
		_show_usage()
		
	#showusage() call above will quit if expected number of arguments not found
	#, so no check is made here		
	
	return True

def test_twitterusers():
	
	t = TwitterUsers(token, token_secret, consumer_key, consumer_secret)
	t.read_user_list_json("data/userlist_train.json")
	#print("Test User list JSON:\n" + str(t.get_user_list()) + "\n")
	
	return t
	
def test_twitterfeatures(t):
	
	f = TwitterFeatures()
	humanbow, botbow = f.extract_features(t)
	return humanbow, botbow
	
if __name__ == "__main__":
	process_cmd(sys.argv)
	t = test_twitterusers()
	humanbow, botbow = test_twitterfeatures(t)
	#print_dictionaries()
	#classify_complexity_metric(humanbow, botbow, t, "@vivekagnihotri")

#end of file
