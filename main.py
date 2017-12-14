""" Copyright @ karthickng@gmail.com.
Main entry point of the botscore program: handles command line processing.
"""

#! /usr/bin/env python

import sys
from twitterfeatures.twitterusers import TwitterUsers
from twitterfeatures.twitterfeatures import TwitterFeatures
#from login import login, loginhelper

def _show_usage():
	""" Print usage help for program. """
	
	print("Usage: botscore <userid>\n")
	sys.exit(0)
	
def process_cmd(args):
	""" Process command line arguments. """
	
	if len(args) != 2:
		_show_usage()
		
	#showusage() call above will quit if expected number of arguments not found
	#, so no check is made here		
	t = TwitterUsers(args)
	for username in ["@RUWT","@jamesmtitus"]:
		t.add_user(username, 'bot')
		
	for username in ["@iasura_","@dww_k", "@ShefVaidya"]:
		t.add_user(username) # default type='human'
	
	print("Test User list programmed:\n" + str(t.get_user_list()) + "\n")
	
	t.set_user_list_json("testdata/users.json")
	print("Test User list JSON:\n" + str(t.get_user_list()) + "\n")
	
	return True

	
if __name__ == "__main__":
		process_cmd(sys.argv)
		#login()
		#loginhelper()