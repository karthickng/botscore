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
	
	if (os.path.isfile("merged_user_list.json")):
		os.remove("merged_user_list.json")
	t = TwitterUsers(token, token_secret, consumer_key, consumer_secret)
	try:
		for username in ["@RUWT","@jamesmtitus"]:
			t.add_user(username, 'bot')
		for username in ["@iasura_","@dww_k", "@ShefVaidya"]:
			t.add_user(username) # default type='human'
		#print("Test User list programmed:\n" + str(t.get_user_list()) + "\n")
	except UserListCreationError:
		print('User list creation error')
	except UserTypeError:
		print('User type error in input\n')
	except:
		print("Unexpected error")
		raise
	
	t.read_user_list_json("testdata/users.json")
	#print("Test User list JSON:\n" + str(t.get_user_list()) + "\n")
	
	t.add_user("@new_user", "bot")
	#print("User list with new addition:\n" + str(t.get_user_list()) + "\n")
	
	t.append_user_list_json("testdata/more_users.json")
	#print("User list with appended list:\n" + str(t.get_user_list()) + "\n")
	
	t.write_user_list_json("merged_user_list.json")
	
	return t
	
def test_twitterfeatures(t):
	
	f = TwitterFeatures()
	humanbow, botbow = f.extract_features(t)
	return humanbow, botbow
	
if __name__ == "__main__":
	process_cmd(sys.argv)
	t = test_twitterusers()
	humanbow, botbow = test_twitterfeatures(t)
	print_dictionaries()
	#classify_complexity_metric(humanbow, botbow, t, "@vivekagnihotri")

#end of file
