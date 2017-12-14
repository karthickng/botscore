'''
Twitter users wrapper
---------------------
'''

from twitter import Twitter, OAuth
import logging
import datetime
import numpy as np
from twitterfeatures.userlist import twitter_bots, twitter_humans
from error import UserTypeError
import json

class TwitterUsers(object):
    '''
    Twitter users (human and bot) manager class
    '''
    
    def login(self):
        """.. todo:: use file or command line input """
        """.. todo:: exception handling """
        self.t = Twitter(auth=OAuth("3018287190-tG4K1NW1OAUMKi1IhKsFn41LwBsnSsYfj0GA6vX", "7zivxHb2ckKEnY3TlWojjLr6Rpcxh5ikQyvGdgaJhAlU8", "BXrC55ZUlvmuuGeLnzIqW4nhr", "Tit9mp5hwG9CbDrOMDywTNKghVOzDQ9wqhCAFKGW8LLBt7IXAt"))   #ToDo- Add authorization, error handling
        pass
    
    def add_user(self, userid, usertype='human'):
        """.. todo:: validate userid, exception handling?"""
        if usertype == 'human':
            twitter_humans.append(userid)
        elif usertype == 'bot':
            twitter_bots.append(userid)
        else:
            raise UserTypeError

    def set_user_list_json(self, user_list_json_file='users.json'):
        """.. todo:: implement """
        from builtins import str
        try:
            f= open(user_list_json_file)
            user_data = json.load(f)
            self._parse_json_user_data(user_data)
        except Exception:
            print("Error reading JSON file:" + str(user_list_json_file))
            raise
        
    def set_human_user_list_csv(self, user_list):
        """.. todo:: implement """
        pass
    
    def set_bot_user_list_csv(self, user_list):
        """.. todo:: implement """
        pass
   
    def get_user_list(self):
        ret_list = twitter_humans + twitter_bots
        """.. todo:: implement type identification?"""
        return ret_list
        pass
    
    def get_user_list_json(self):
        """.. todo:: implement """
        pass
    
    def get_human_user_list_csv(self):
        """.. todo:: implement """
        pass
    
    def get_bot_user_list_csv(self):
        """.. todo:: implement """
        pass    
       
    def _get_oauth(self):
        """.. todo:: read from file
        """
        
        __oauth_token = 'STULycatgreF6VTWhvdhzR1CiInb9WtATgRz31tmGxCIr'
        __oauth_token_secret = '3018287190-djFisoik8d1mRoSRawwpsyOCwq4KUetDzmYknhF'
        __consumer_key = ''
        __consumer_secret = ''
        
    def _parse_json_user_data(self, user_data):
        twitter_humans.clear()
        for s in user_data['humanusers']:
            twitter_humans.append(s['name'])
        twitter_bots.clear()
        for s in user_data['botusers']:
            twitter_bots.append(s['name'])
        
    def __init__(self, params):
        '''
        Constructor
        '''
        
        self.login()
        from builtins import str
        previnstant = currinstant = datetime.datetime.strptime("2017-12-13 18:34:00 +0000",'%Y-%m-%d %H:%M:%S +0000')
        if len(params) > 3:
            logging.error('Incorrect parameters')
            exit(0)
        else:
            pass
        """
            print("Twitter bots stats:\n")
            for userid in twitter_bots:
                print("User ID is " + userid)
                
                x= self.t.statuses.user_timeline(screen_name=userid )
                #print('Length of timeline is: '+ str(len(x)))
                time_between_tweets_sec = []
                for i in range(len(x)):
                    #print(ts)
                    previnstant = currinstant
                    currinstant = datetime.datetime.strptime(x[i]['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                    diffintime = previnstant - currinstant
                    time_between_tweets_sec.append(diffintime.total_seconds())
                    
                mean_intertweet_period = np.mean(time_between_tweets_sec)
                std_intertweet_period = np.std(time_between_tweets_sec)
                print("Mean = " + str(mean_intertweet_period) + ", SD = " + str(std_intertweet_period))
                
            print("\n\nTwitter humans stats:\n")
            for userid in twitter_humans:
                print("User ID is " + userid)
                t = Twitter(auth=OAuth("3018287190-tG4K1NW1OAUMKi1IhKsFn41LwBsnSsYfj0GA6vX", "7zivxHb2ckKEnY3TlWojjLr6Rpcxh5ikQyvGdgaJhAlU8", "BXrC55ZUlvmuuGeLnzIqW4nhr", "Tit9mp5hwG9CbDrOMDywTNKghVOzDQ9wqhCAFKGW8LLBt7IXAt"))   #ToDo- Add authorization, error handling
                x= t.statuses.user_timeline(screen_name=userid )
                #print('Length of timeline is: '+ str(len(x)))
                time_between_tweets_sec = []
                for i in range(len(x)):
                    #print(ts)
                    previnstant = currinstant
                    currinstant = datetime.datetime.strptime(x[i]['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                    diffintime = previnstant - currinstant
                    time_between_tweets_sec.append(diffintime.total_seconds())
                    
                mean_intertweet_period = np.mean(time_between_tweets_sec)
                std_intertweet_period = np.std(time_between_tweets_sec)
                print("Mean = " + str(mean_intertweet_period) + ", SD = " + str(std_intertweet_period))
                """
        #print(self.twitterApi.VerifyCredentials())
            
