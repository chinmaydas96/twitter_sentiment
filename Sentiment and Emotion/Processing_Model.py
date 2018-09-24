#start process_tweet
def processTweet(tweet):
    import re
    # process the tweets
    #Convert to lower case
    try:
        tweet = tweet.lower()
    except:
        print('Cannot Convert to lower')
    
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

def lemmatizeTweet(tweet):
    from nltk.stem.wordnet import WordNetLemmatizer
    lemmatizer=WordNetLemmatizer()
    from nltk.tokenize import word_tokenize
    tokens=word_tokenize(tweet)
    temp_tweet_v=[lemmatizer.lemmatize(t.lower(),'v') for t in tokens]
    temp_tweet_a=[lemmatizer.lemmatize(t.lower(),'a') for t in temp_tweet_v]
    temp_tweet_n=[lemmatizer.lemmatize(t.lower(),'n') for t in temp_tweet_a]
    print(temp_tweet_n)
    temp_tweet=''
    for i in temp_tweet_n:
        temp_tweet+=i+' '
    return temp_tweet

#print(lemmatizeTweet('Hi, I am happy'))