'''
Created on 06-Feb-2018

@author: ngk
'''

'''
Tests
------------------------
'''

import os

def print_dictionaries():
    from gensim.corpora.dictionary import Dictionary
    d = Dictionary()
    if os.path.isfile("bot_dictionary"):
        d.load("bot_dictionary")
        print(d.token2id)
    else:
        print("Bot dictionary not found")