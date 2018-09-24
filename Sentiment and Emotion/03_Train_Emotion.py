#import os
import pandas as pd
from Processing_Model import processTweet
from Processing_Model import lemmatizeTweet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from twitter_get_data import query_str

#Preparing Data for training
tweets=[]
type_emotion=[]
data=pd.read_csv('text_emotion.csv',encoding="ISO-8859-1")
for j in range(len(data)):
        data.iloc[:,3][j]=processTweet(data.iloc[:,3][j])
        data.iloc[:,3][j]=lemmatizeTweet(data.iloc[:,3][j])
        tweets.append(data.iloc[:,3][j])
        type_emotion.append(data.iloc[:,1][j])

data_processed=pd.DataFrame({'Tweets':tweets,'Emotion':type_emotion})

le=LabelEncoder()
data_processed.iloc[:,0]=le.fit_transform(data_processed.iloc[:,0])

from nltk.corpus import stopwords
stop_words=stopwords.words('english')
stop_words.append('at_user')
stop_words.append('url')

tfidf_vect=TfidfVectorizer(max_df=0.98,min_df=0.02,stop_words=stop_words,token_pattern="\w+(?:[-']\w+)?",ngram_range=(1,3))
response=tfidf_vect.fit_transform(data_processed.iloc[:,1])


from sklearn.svm import SVC
svc=SVC()
svc.fit(X=response,y=data_processed.iloc[:,0])

import os
path=os.getcwd()
os.chdir(query_str)
data=pd.read_csv('emotion_results.csv')
for j in range(len(data)):
    data.iloc[:,0][j]=processTweet(data.iloc[:,0][j])
    data.iloc[:,0][j]=lemmatizeTweet(data.iloc[:,0][j])

response_test = tfidf_vect.transform(data.iloc[:,0])
predictions=svc.predict(response_test)
data.loc[:,'Emotion_Prediction']=le.inverse_transform(predictions)
data.to_csv('Predicted_Emotions.csv',index=None)

'''
For Facebook Data
Using Trained model data is transformed
'''

data_fb=pd.read_csv('Facebook_data.csv',encoding='ISO-8859-1')
for j in range(len(data_fb)):
    data_fb.iloc[:,1][j]=processTweet(data_fb.iloc[:,1][j])
    data_fb.iloc[:,1][j]=lemmatizeTweet(data_fb.iloc[:,1][j])

response_test = tfidf_vect.transform(data_fb.iloc[:,1])
predictions=svc.predict(response_test)
data_fb.loc[:,'Emotion_Prediction']=le.inverse_transform(predictions)
data_fb.to_csv('Predicted_Emotions_FB.csv',index=None,encoding='ISO-8859-1')
os.chdir(path)