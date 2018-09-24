import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)
data_twitter=pd.read_csv('Final_Results.csv',encoding='ISO-8859-1')
data_happiness=[]  
data_sad=[]  
data_worry=[]  
data_angry=[]  
data_relief=[]  
data_surprise=[]  
data_neutral=[]  
data_love=[]  
data_hate=[]  
data_boredom=[]  
data_empty=[]  
data_enthusiasm=[]  
data_fun=[]  
for i in range(0,len(data_twitter)):
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='worry'):
        data_worry.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='sadness'):
        data_sad.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='happiness'):
        data_happiness.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='anger'):
        data_angry.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='relief'):
        data_relief.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='boredom'):
        data_boredom.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='love'):
        data_love.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='hate'):
        data_hate.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='enthusiasm'):
        data_enthusiasm.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='empty'):
        data_empty.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='neutral'):
        data_neutral.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='surprise'):
        data_surprise.append(data_twitter.loc[:,'Text'][i])
    if(data_twitter.loc[:,'Emotion_Prediction'][i]=='fun'):
        data_fun.append(data_twitter.loc[:,'Text'][i])
    
stop_words=pd.read_fwf(path+'\\stopwords_en.txt',header=None)[0].tolist()
stop_words.append('at_user')
stop_words.append('url')

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect=TfidfVectorizer(max_df=0.95,min_df=0.02,stop_words=stop_words,ngram_range=(1,3))
response_matrix=tfidf_vect.fit_transform(data_twitter.loc[:,'Text'])
import numpy as np
indices = np.argsort(tfidf_vect.idf_)[::-1]
features = tfidf_vect.get_feature_names()
top_n = 10
top_features = [features[i] for i in indices[:top_n]]
file=open('Word_Cloud.txt','w',encoding='ISO-8859-1')
for i in top_features:
    file.writelines(i+'\n')
file.close()
 

#For Worry
if(len(data_worry)>0):
    tfidf_vect=TfidfVectorizer(max_df=0.95,min_df=0.02,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_worry)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_worry.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Worry_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()



#For Angry
if(len(data_angry)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_angry)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_angry.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Angry_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()


#For Sadness
if(len(data_sad)>0):
    tfidf_vect=TfidfVectorizer(max_df=0.95,min_df=0.02,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_sad)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_sad.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Sad_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()

#For happiness
if(len(data_happiness)>0):
    tfidf_vect=TfidfVectorizer(max_df=0.95,min_df=0.02,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_happiness)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_happiness.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_happiness_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()


#For Love
if(len(data_love)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_love)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_love.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_love_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()
    
    
#For Hate
if(len(data_hate)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_hate)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_hate.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Hate_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()


#For Relief
if(len(data_relief)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_relief)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_relief.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Relief_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()


#For Fun
if(len(data_fun)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_fun)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_fun.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Fun_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()


#For Enthusiasm
if(len(data_enthusiasm)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_enthusiasm)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_enthusiasm.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Enthusiasm_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()
    
#For Surprise
if(len(data_surprise)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_surprise)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_surprise.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Surprise_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()

#For Empty
if(len(data_empty)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_empty)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_empty.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Empty_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()

#For Angry
if(len(data_neutral)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_neutral)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_neutral.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Neutral_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()

#For Boredom
if(len(data_boredom)>0):
    tfidf_vect=TfidfVectorizer(max_df=1,min_df=0,stop_words=stop_words,ngram_range=(1,3))
    response_matrix=tfidf_vect.fit_transform(data_boredom)
    indices = np.argsort(tfidf_vect.idf_)[::-1]
    features = tfidf_vect.get_feature_names()
    top_n = 200
    top_features = [features[i] for i in indices[:top_n]]
    file=open('Word_Cloud_for_Boredom.txt','w',encoding='ISO-8859-1')
    for i in top_features:
        file.writelines(i+'\n')
    file.close()
    file_vocab=open('Word_Cloud_Boredom_Vocab.txt','w',encoding='ISO-8859-1')
    for i in tfidf_vect.vocabulary_:
        file_vocab.writelines(i+'\n')
    file_vocab.close()
os.chdir(path)