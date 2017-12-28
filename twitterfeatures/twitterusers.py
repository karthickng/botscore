'''
Twitter users wrapper
---------------------
'''

from twitter import Twitter, OAuth
from twitterfeatures.userlist import twitter_bots, twitter_humans
from error import UserTypeError
import json

class TwitterUsers(object):
    '''
    Twitter users (human and bot) manager class
    '''
    
    def login(self, token, token_secret, consumer_key, consumer_secret):
        ''' Login and initialize the Twitter API object '''
        self.token = token
        self.token_secret = token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        
        try:
            self.twitter_object = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))   #ToDo- Add authorization, error handling
        except Exception:
            print('Error logging in to Twitter')
            print('Ensure valid Twitter credentials. Refer https://apps.twitter.com/')
            raise
    
    def add_user(self, userid, usertype='human'):
        ''' Add one user to the Twitter user list '''
        from builtins import str
        """.. todo:: validate userid(?), duplicate handling, exception handling here(?)"""
        if usertype == 'human':
            if (userid in twitter_humans):
                print(str(userid) + ' is already in human user list')
                return
            twitter_humans.append(userid)
        elif usertype == 'bot':
            if (userid in twitter_bots):
                print(str(userid) + ' is already in bot user list')
                return
            twitter_bots.append(userid)
        else:
            raise UserTypeError

    def read_user_list_json(self, user_list_json_filename='users.json'):
        ''' Initialize a new Twitter user list from JSON file '''
        from builtins import str
        try:
            f= open(user_list_json_filename,'rt')
            user_data = json.load(f)
            """.. todo:: JSON structure(?) check?"""
            twitter_humans.clear()
            twitter_bots.clear()
            self._append_json_user_data(user_data)
            f.close()
        except Exception:
            print("Error creating user list from JSON file:" + str(user_list_json_filename))
            '''.. todo:: try to close file on exception?? '''
            raise
        
    def append_user_list_json(self, user_list_json_filename='users.json'):
        ''' Append Twitter user list to existing user list from JSON file
            Use along with write_user_list_json to add new users to merge to existing JSON user file'''
        try:
            f= open(user_list_json_filename,'r')
            user_data = json.load(f)
            self._append_json_user_data(user_data)
            f.close()
        except Exception:
            print("Error reading JSON file:" + str(user_list_json_filename))
            '''.. todo:: try to close file on exception?? '''
            raise
        
    def set_human_user_list_csv(self, user_list):
        """.. todo:: implement """
        pass
    
    def set_bot_user_list_csv(self, user_list):
        """.. todo:: implement """
        pass
   
    def get_user_list(self):
        ret_list = twitter_humans + twitter_bots
        return ret_list
    
    def get_human_list(self):
        return twitter_humans
    
    def get_bot_list(self):
        return twitter_bots
    
    def write_user_list_json(self,user_list_json_filename="userlist.json"):
        write_list = {}
        write_list["humanusers"] = twitter_humans
        write_list["botusers"] = twitter_bots
        try:
            with open(user_list_json_filename, "xt") as outfile:
                json.dump(write_list, outfile, indent=4)
        except Exception:
            print("Error reading JSON file:" + str(user_list_json_filename))
            '''.. todo:: try to close file on exception?? '''
            raise
    
    def get_human_user_list_csv(self):
        """.. todo:: implement """
        pass
    
    def get_bot_user_list_csv(self):
        """.. todo:: implement """
        pass    
       
    def _get_oauth(self):
        oauth_details = []
        oauth_details.append(self.token)
        oauth_details.append(self.token_secret)
        oauth_details.append(self.consumer_key)
        oauth_details.append(self.consumer_secret)
        return oauth_details
        
    def _append_json_user_data(self, user_data):
        for s in user_data['humanusers']:
            if (s in twitter_humans):
                print(str(s) + ' is already in human user list')
                continue
            twitter_humans.append(s)
        for s in user_data['botusers']:
            if (s in twitter_bots):
                print(str(s) + ' is already in bot user list')
                continue
            twitter_bots.append(s)
        
    def __init__(self, token, token_secret, consumer_key, consumer_secret):
        '''
        Constructor
        '''
        try:
            self.login(token, token_secret, consumer_key, consumer_secret)
        except Exception:
            print("Unable to create a Twitter users object\nError logging in")
            

#end of file
            
