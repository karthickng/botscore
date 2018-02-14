'''
Twitter features wrapper
------------------------
'''

from twitterfeatures.twitterusers import TwitterUsers
from twitter import Twitter
from gensim.corpora.dictionary import Dictionary
import os

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
        return self.human_bow_vectors, self.bot_bow_vectors
        
    def _get_tweet_list(self, t):
        """Get tweet list by accounts in human and bot list """
        """.. todo:: This function must be rewritten to accommodate iterating from a larger account list """
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
            
        print('Number of human accounts: ' +str(len(humans))+", Number of bot accounts: "  +str(len(bots)))
        print('Number of human tweets: ' + str(len(self.raw_human_tweets))+', Number of bot tweets: ' + str(len(self.raw_bot_tweets)))
        
    def _preprocess_tweets(self):
        """Preprocess tweets before feature extraction"""
        
        # Create a set of frequent words to remove
        stoplist = set('a an the is was were and or not for of with without to from has have had in out as'.split(' '))
       
#process human tweets 
        # Lowercase each document, split it by white space and filter out stopwords
        humantexts = [[word for word in document.lower().split() if word not in stoplist] 
                 for document in self.raw_human_tweets]
        
        pre_processed_text = []
        
        for text in humantexts:
            result = []
            for token in text:
                #Remove all references to Twitter accounts and hashtags(?)
                if token.startswith('@') or token.startswith('#'):
                    text.remove(token)
                    continue
                #Remove all hyperlinks
                #todo: use regexp
                if 'http' in token: #basic check, will remove even regular tokens which have substring 'http'
                    text.remove(token)
                    continue
                #Remove common trailing characters to reduce number of words in dictionary
                #todo:reduce memory needed
                while token.endswith('.') or token.endswith(' ') or token.endswith(',')  or \
                token.endswith(';')  or token.endswith('!')  or token.endswith('?') or token.endswith('+') or token.endswith('-') or \
                token.endswith(')') or token.endswith('%')  or token.endswith('&'):
                    token = token[:-1]
                    
                #Remove common leading characters to reduce number of words in dictionary
                #todo:reduce memory needed
                while token.startswith('.') or token.startswith(' ') or token.startswith(',')  or \
                token.startswith(';')  or token.startswith('!')  or token.startswith('?') or token.startswith('+') or token.startswith('-') or \
                token.startswith('(') or token.startswith('$')  or token.startswith('&'):
                    token = token[1:]
                
                if token == '':
                    continue    
                #print(token)
                result.append(token)
                
            pre_processed_text.append(result)
                
        humantexts = pre_processed_text
        '''.. todo: add stemming '''
        '''for text in texts:
            for token in text:
                stemmed_token = parsing.stem_text(token)
                #print(stemmed_token)
            ... todo: stemming '''
        
        #Tokenize the collection of tweets            
        from collections import defaultdict
        wordfrequencyhuman = defaultdict(int)
        for text in humantexts:
            for token in text:
                wordfrequencyhuman[token] += 1
                
        #Only words used more than once are considered
        # Todo: revisit this based on  data
        processed_corpus_humans = [[token for token in text if wordfrequencyhuman[token] > 1] for text in humantexts]
        
        from pprint import pprint
        f= open('processed_human_corpus',mode='w')
        pprint(processed_corpus_humans, stream=f)
        
        human_dictionary = Dictionary()
        if os.path.isfile("human_dictionary"):
            #print("Human dictionary exists")
            human_dictionary.load("human_dictionary")
        #human_dictionary = corpora.Dictionary(processed_corpus_humans)
        human_dictionary.add_documents(processed_corpus_humans)
        try:
            human_dictionary.save("human_dictionary")
        except Exception:
            print("Unable to save human dictionary file")
                
        self.human_bow_vectors = [human_dictionary.doc2bow(text) for text in processed_corpus_humans]
        print(human_dictionary)
        f= open('processed_human_dictionary',mode='w')
        pprint(human_dictionary.token2id, stream=f)
        f= open('human_vectors',mode='w')
        pprint(self.human_bow_vectors, stream=f)

#process bot tweets
        # Lowercase each document, split it by white space and filter out stopwords
        bottexts = [[word for word in document.lower().split() if word not in stoplist] 
                 for document in self.raw_bot_tweets]
        
        pre_processed_text = []
        for text in bottexts:
            result = []
            for token in text:
                #Remove all references to Twitter accounts
                if token.startswith('@'):
                    text.remove(token)
                    continue
                #Remove all hyperlinks
                if 'http' in token:
                    text.remove(token)
                    continue
                #Remove common trailing characters to reduce number of words in dictionary
                #todo:reduce memory needed
                while token.endswith('.') or token.endswith(' ') or token.endswith(',')  or \
                token.endswith(';')  or token.endswith('!')  or token.endswith('?') or token.endswith('+') or token.endswith('-') or \
                token.endswith(')') or token.endswith('%')  or token.endswith('&'):
                    token = token[:-1]
                    
                #Remove common leading characters to reduce number of words in dictionary
                #todo:reduce memory needed
                while token.startswith('.') or token.startswith(' ') or token.startswith(',')  or \
                token.startswith(';')  or token.startswith('!')  or token.startswith('?') or token.startswith('+') or token.startswith('-') or \
                token.startswith('(') or token.startswith('$')  or token.startswith('&'):
                    token = token[1:]
                
                if token == '':
                    continue
                
                #print(token)
                result.append(token)
                
            pre_processed_text.append(result)
            
        bottexts = pre_processed_text        
        '''for text in texts:
            for token in text:
                stemmed_token = parsing.stem_text(token)
                #print(stemmed_token)
            ... todo: stemming '''
        
        #Tokenize the collection of tweets            
        wordfrequencybot = defaultdict(int)
        for text in bottexts:
            for token in text:
                wordfrequencybot[token] += 1
                
        #Only words used more than once are considered
        # Todo: revisit this based on  data
        processed_corpus_bots = [[token for token in text if wordfrequencybot[token] > 1] for text in bottexts]
        
        f= open('processed_bot_corpus',mode='w')
        pprint(processed_corpus_bots, stream=f)
        
        bot_dictionary = Dictionary()
        #bot_dictionary = corpora.Dictionary(processed_corpus_bots)
        if os.path.isfile("bot_dictionary"):
            #print("Bot dictionary exists")
            bot_dictionary.load("bot_dictionary")
        #human_dictionary = corpora.Dictionary(processed_corpus_humans)
        bot_dictionary.add_documents(processed_corpus_bots)
        try:
            bot_dictionary.save("bot_dictionary")
        except Exception:
            print("Unable to save bot dictionary file")
        
        self.bot_bow_vectors = [bot_dictionary.doc2bow(text) for text in processed_corpus_bots]
        print(bot_dictionary)
        f= open('processed_bot_dictionary',mode='w')
        pprint(bot_dictionary.token2id, stream=f)
        f= open('bot_vectors',mode='w')
        pprint(self.bot_bow_vectors, stream=f)
    
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