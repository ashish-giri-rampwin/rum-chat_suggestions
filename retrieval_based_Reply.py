import nltk
import random
import string
import re
import dateparser
import sys

from dateparser.search import search_dates
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from classes_dict import classes_dict,date_re,time_re


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def pos_tagging(txt):
    tokenized = sent_tokenize(txt)
    for i in tokenized:
        
        # Word tokenizers is used to find the words 
        # and punctuation in a string
        wordsList = nltk.word_tokenize(i)
    
        # removing stop words from wordList
    
        #  Using a Tagger. Which is part-of-speech 
        # tagger or POS-tagger. 
        tagged = nltk.pos_tag(wordsList)
    
        print(tagged)
    return tagged

def lem_tokens(tokens):

    lemmer = nltk.stem.WordNetLemmatizer()

    return [lemmer.lemmatize(token) for token in tokens]

def lem_normalize(text):
    return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    # return LemTokens(nltk.word_tokenize(text.lower()))

def my_response(user_input):
    robo_response = ''
    sent_tokens, word_tokens = post_dict(classes_dict)

    #sent_tokens.append(user_response)
    sent_tokens['user'] = user_input

    sent_tokens_ = []

    for value in sent_tokens:
        sent_tokens_.append(sent_tokens[value])

    # tfidf_vec = TfidfVectorizer(tokenizer = lem_normalize, stop_words='english')
    tfidf_vec = TfidfVectorizer(tokenizer = lem_normalize)
    tfidf = tfidf_vec.fit_transform(sent_tokens_)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    # print req_tfidf

    error_threshold = 0.1
    if re.search(date_re, user_input):
        event_time=re.search(date_re,user_input).group()
        print(event_time)
        event_time=dateparser.parse(event_time)
        robo_response = {"type" : "action","action" : "schedule_a_followup","parameters" : { "event_time" : event_time}}
        return robo_response
    elif re.search(time_re, user_input):
        event_time=re.search(time_re,user_input).group()
        print(event_time)
        event_time=dateparser.parse(event_time)
        robo_response = {"type" : "action","action" : "schedule_a_followup","parameters" : { "event_time" : event_time}}
        return robo_response
    elif(req_tfidf < error_threshold):
        robo_response = ["[No Suggestion]"]
        return robo_response
    
    else:
        if idx==3:
            robo_response = {"type" : "action","action" : "create_ticket","parameters" : { "Tags" : ""}}
            return robo_response
            
        elif idx==4:
            for value in sent_tokens:
                match_pattern = sent_tokens_[idx]
                pattern = sent_tokens[value]
                if match_pattern == pattern:
                    match_class = value
        # print match_clase
            robo_response = {"type" : "action","action" : "schedule_a_followup","parameters" : { "event_time" : event_time}}
            return robo_response
        else:
            
            for value in sent_tokens:
                match_pattern = sent_tokens_[idx]
                pattern = sent_tokens[value]
                if match_pattern == pattern:
                    match_class = value

    
        # print match_clase
        
            robo_response = {"type" : "smalltalk","responses" : classes_dict[match_class]['response']}
            return robo_response

def post_dict(some_dict):

    sent_tokens = {}

    for value in some_dict:
        words = some_dict[value]["pattern"]
        words = ' '.join(words)
        sent_tokens[value] = words
        word_tokens = nltk.word_tokenize(words)

    return sent_tokens, word_tokens



# # flag = True

# # while flag:
# #     user_input=input(">>>")
# #     if(user_input != "quit"):

# #         response = my_response(classes_dict, user_input, sent_tokens)
# #         for i in range(0, len(response)):
# #             print('* ' + response[i])
# #         # sent_tokens.remove(user_input)
# #         del sent_tokens['user']
# #     else:
#         flag = False


# nltk.download('punkt')
# nltk.download('wordnet')


print(dateparser.parse())