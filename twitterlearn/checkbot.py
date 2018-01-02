'''
Functions to classify a Twitter account as a bot or not 
Created on 29-Dec-2017

@author: ngk
'''

from gensim import similarities, models

def classify_complexity_metric(humanbow, botbow, t, username):
    #print('Human index: ' + str(human_index_) + ', Bot index: ' + str(bot_index_))
    print("Entered classify::::::::::::::::::::::::::::::::::::::::::::::")
    test_tweets=[]
    try:
        d = t.twitter_object.statuses.user_timeline(screen_name=username,  count= 200, include_rts = False)
        for i in d:
            #print(i['text'])
            test_tweets.append(i['text'])
            
        stoplist = set('a an the is was were and or not for of with without to from has have had in out as'.split(' '))
       
#process human tweets 
        # Lowercase each document, split it by white space and filter out stopwords
        texts_ = [[word for word in document.lower().split() if word not in stoplist] 
                 for document in test_tweets]
        
        for text in texts_:
            for token in text:
                #Remove all references to Twitter accounts
                if token.startswith('@'):
                    text.remove(token)
                    continue
                #Remove all hyperlinks
                #todo: use regexp
                if 'http' in token: #basic check, will remove even regular tokens which have substring 'http'
                    text.remove(token)
        
        #Tokenize the collection of tweets            
        from collections import defaultdict
        wordfrequency = defaultdict(int)
        for text in texts_:
            for token in text:
                wordfrequency[token] += 1
                
        #Only words used more than once are considered
        # Todo: revisit this based on  data
        processed_test_text = [[token for token in text if wordfrequency[token] > 1] for text in texts_]
        #print(processed_test_text)
        
        from gensim import corpora
        dictionary = corpora.Dictionary(processed_test_text)
        texts_bow_vectors = [dictionary.doc2bow(text) for text in processed_test_text]
        #print(texts_bow_vectors)
            
        #m = models.basemodel(humanbow)
        #print(m)
        tfidf = models.TfidfModel(humanbow)
        transformed_text_vectors = tfidf[texts_bow_vectors]
        #print(transformed_text_vectors)
        
        human_index_ = similarities.MatrixSimilarity(tfidf[humanbow])
        bot_index_ = similarities.MatrixSimilarity(tfidf[botbow])
        #print(human_index_)
        sims = human_index_[transformed_text_vectors[0]]
        print(list(enumerate(sims)))
        '''for i in d:
            sims = human_index_[i['text']]
            print(sims)'''
    except Exception:
        print('Error checking tweets from ' + str(username))

    