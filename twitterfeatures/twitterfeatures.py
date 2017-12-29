'''
Twitter features wrapper
------------------------
'''

from twitterfeatures.twitterusers import TwitterUsers
from twitter import Twitter

class TwitterFeatures(object):
    '''
    Twitter features manager class
    '''
    """ Max number of tweets used from a single account to extract the features """
    MAX_TWEETS_PER_ACCOUNT = 200
    
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
    
    def extract_features(self, t):
        self._get_tweet_list(t) #in self.raw_human_tweets and self.raw_bot_tweets
        self._preprocess_tweets()
        return self.human_bow_corpus, self.bot_bow_corpus
        
        
    def _get_tweet_list(self, t):
        """Get tweet list by accounts in human and bot list """
        self.raw_human_tweets = []
        self.raw_bot_tweets = []
        
        humans = t.get_human_list()
        bots = t.get_bot_list()     
        
        for usernames in humans:
            try:
                d = t.twitter_object.statuses.user_timeline(screen_name=usernames,  count= self.MAX_TWEETS_PER_ACCOUNT, include_rts = False)
                for i in d:
                    self.raw_human_tweets.append(i['text'])
            except Exception:
                print('Error getting tweets from ' + str(usernames))
                print('Check user ID: ' + str(usernames))
                continue
            
        for usernames in bots:
            try:
                d = t.twitter_object.statuses.user_timeline(screen_name=usernames,  count= self.MAX_TWEETS_PER_ACCOUNT, include_rts = False)
                for i in d:
                    self.raw_bot_tweets.append(i['text'])
            except Exception:
                print('Error getting tweets from user ID: ' + str(usernames))
                continue
            
        print('Number of human tweets: ' +str(len(self.raw_human_tweets)))
        print('Number of bot  tweets: ' +str(len(self.raw_bot_tweets)))
        
    def _preprocess_tweets(self):
        """Preprocess tweets before feature extraction"""
        
        # Create a set of frequent words to remove
        stoplist = set('for a of the and to in is was has have with as'.split(' '))
       
#process human tweets 
        # Lowercase each document, split it by white space and filter out stopwords
        humantexts = [[word for word in document.lower().split() if word not in stoplist] 
                 for document in self.raw_human_tweets]
        
        from gensim import parsing
        for text in humantexts:
            for token in text:
                #Remove all references to Twitter accounts
                if token.startswith('@'):
                    text.remove(token)
                #Remove all hyperlinks
                #todo: use regexp
                if 'http' in token: #basic check, will remove even regular text which has substring 'http'
                    text.remove(token)
        '''for text in texts:
            for token in text:
                stemmed_token = parsing.stem_text(token)
                #print(stemmed_token)
            ... todo: stemming '''
                    
        from collections import defaultdict
        wordfrequencyhuman = defaultdict(int)
        for text in humantexts:
            for token in text:
                wordfrequencyhuman[token] += 1
                
        #Only words used more than once are considered
        # Todo: revisit this based on  data
        processed_corpus_humans = [[token for token in text if wordfrequencyhuman[token] > 1] for text in humantexts]
        
        from gensim import corpora
        human_dictionary = corpora.Dictionary(processed_corpus_humans)
        self.human_bow_corpus = [human_dictionary.doc2bow(text) for text in processed_corpus_humans]

#process bot tweets
        # Lowercase each document, split it by white space and filter out stopwords
        bottexts = [[word for word in document.lower().split() if word not in stoplist] 
                 for document in self.raw_bot_tweets]
        
        from gensim import parsing
        for text in bottexts:
            for token in text:
                #Remove all references to Twitter accounts
                if token.startswith('@'):
                    text.remove(token)
                #Remove all hyperlinks
                if 'http' in token:
                    text.remove(token)
        '''for text in texts:
            for token in text:
                stemmed_token = parsing.stem_text(token)
                #print(stemmed_token)
            ... todo: stemming '''
                    
        from collections import defaultdict
        wordfrequencybot = defaultdict(int)
        for text in bottexts:
            for token in text:
                wordfrequencybot[token] += 1
                
        #Only words used more than once are considered
        # Todo: revisit this based on  data
        processed_corpus_bots = [[token for token in text if wordfrequencybot[token] > 1] for text in bottexts]
            
        from gensim import corpora
        bot_dictionary = corpora.Dictionary(processed_corpus_bots)
        self.bot_bow_corpus = [bot_dictionary.doc2bow(text) for text in processed_corpus_bots]

    
"""  todo: use below code when needed   
    
    previnstant = currinstant = datetime.datetime.strptime("2017-12-13 18:34:00 +0000",'%Y-%m-%d %H:%M:%S +0000')
        if len(params) > 3:
            logging.error('Incorrect parameters')
            exit(0)
        else:
            pass
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