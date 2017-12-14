""" Copyright @ karthickng@gmail.com.
Twitter wrapper
"""

from twitter import *
import logging
import datetime
import numpy as np
from TwitterFeatures.userlist import *



class TwitterWrapper(object):
    '''
    class that abstracts a feature extracted from Twitter
    '''
    
    def _get_oauth(self):
        #todo: read from file
        __oauth_token = 'STULycatgreF6VTWhvdhzR1CiInb9WtATgRz31tmGxCIr'
        __oauth_token_secret = '3018287190-djFisoik8d1mRoSRawwpsyOCwq4KUetDzmYknhF'
        __consumer_key = ''
        __consumer_secret = ''
        
    def __init__(self, params):
        '''
        Constructor
        '''
        from builtins import str
        previnstant = currinstant = datetime.datetime.strptime("2017-12-13 18:34:00 +0000",'%Y-%m-%d %H:%M:%S +0000')
        if len(params) > 3:
            logging.error('Incorrect parameters')
            exit(0)
        else:
            print("Twitter bots stats:\n")
            for userid in twitter_bots:
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
                
        #print(self.twitterApi.VerifyCredentials())
        
    def get_features(self):
        #self.twitterApi
        pass
        
          

            