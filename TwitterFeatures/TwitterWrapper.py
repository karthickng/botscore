'''
Created on 12-Dec-2017

@author: ngk
'''

from twitter import *
import logging
import time


class TwitterWrapper(object):
    '''
    class that abstracts a feature extracted from Twitter
    '''
    
    def getOauth(self):
        #todo: read from file
        __oauth_token = 'STULycatgreF6VTWhvdhzR1CiInb9WtATgRz31tmGxCIr'
        __oauth_token_secret = '3018287190-djFisoik8d1mRoSRawwpsyOCwq4KUetDzmYknhF'
        __consumer_key = ''
        __consumer_secret = ''
        
    def __init__(self, params):
        '''
        Constructor
        '''
        if len(params) > 3:
            logging.error('Incorrect parameters')
            exit(0)
        else:
            print("User ID is " + params[1])
            t = Twitter(auth=OAuth("3018287190-tG4K1NW1OAUMKi1IhKsFn41LwBsnSsYfj0GA6vX", "7zivxHb2ckKEnY3TlWojjLr6Rpcxh5ikQyvGdgaJhAlU8", "BXrC55ZUlvmuuGeLnzIqW4nhr", "Tit9mp5hwG9CbDrOMDywTNKghVOzDQ9wqhCAFKGW8LLBt7IXAt"))   #ToDo- Add authorization, error handling
            x= t.statuses.user_timeline(screen_name="iAsura_")
            for i in range(len(x)):
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(x[i]['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                print(ts)
        #print(self.twitterApi.VerifyCredentials())
        
    def getFeatures(self):
        #self.twitterApi
        pass
        
          

            