'''
Twitter features wrapper
------------------------
'''

class TwitterFeatures(object):
    '''
    Twitter features manager class
    '''
    
    def __init__(self, user_list=[]):
        """.. todo:: implement """
        pass
    
    def add_master_feature(self, description_, calc_function):
        """.. todo:: implement """
        pass
    
    def remove_master_feature(self, feature_id):
        """.. todo:: implement """
        pass
    
    def get_master_features_list(self):
        """.. todo:: implement """
        pass
    
    def select_feature(self, feature_id_list=['all']):
        """.. todo:: implement """
        pass
    
    def get_selected_features(self):
        """.. todo:: implement """
        pass
    
    def remove_feature(self, feature_id):
        """.. todo:: implement """
        pass
    
    def get_feature_description(self, feature_id):
        """.. todo:: implement """
        pass
    
    def get_all_features_description(self):
        """.. todo:: implement """
        pass
    
    
    '''previnstant = currinstant = datetime.datetime.strptime("2017-12-13 18:34:00 +0000",'%Y-%m-%d %H:%M:%S +0000')
        if len(params) > 3:
            logging.error('Incorrect parameters')
            exit(0)
        else:
            pass
'''        """
            print("Twitter bots stats:\n")
            for userid in twitter_bots:
                print("User ID is " + userid)
                
                x= self.t.statuses.user_timeline(screen_name=userid, count= 100 )
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
                x= t.statuses.user_timeline(screen_name=userid, count= 100 )
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
