from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Predicted_Emotions.csv',encoding='ISO-8859-1')
sentiment_scores=[]
sentiment_type=[]
sie=SentimentIntensityAnalyzer()
for i in range(len(data)):
    returned_tweet=data.iloc[:,0][i]
    if(not pd.isnull(returned_tweet)):
        senti_score=sie.polarity_scores(returned_tweet)['compound']
        sentiment_scores.append(senti_score)
        if(senti_score>0.0):
            sentiment_type.append('Positive')
        elif(senti_score<0.0):
            sentiment_type.append('Negative')
        else:
            sentiment_type.append('Neutral')
        
    else:
        sentiment_scores.append(0.0)
        sentiment_type.append('Neutral')

data.loc[:,'Sentiment']=sentiment_scores
data.loc[:,'Sentiment_Type']=sentiment_type 
data.to_csv('Final_Results.csv',index=None)

data=pd.read_csv('Predicted_Emotions_FB.csv',encoding='ISO-8859-1')
sentiment_scores=[]
sentiment_type=[]
sie=SentimentIntensityAnalyzer()
for i in range(len(data)):
    returned_tweet=data.iloc[:,1][i]
    if(not pd.isnull(returned_tweet)):
        senti_score=sie.polarity_scores(returned_tweet)['compound']
        sentiment_scores.append(senti_score)
        if(senti_score>0.0):
            sentiment_type.append('Positive')
        elif(senti_score<0.0):
            sentiment_type.append('Negative')
        else:
            sentiment_type.append('Neutral')
        
    else:
        sentiment_scores.append(0.0)
        sentiment_type.append('Neutral')

data.loc[:,'Sentiment']=sentiment_scores
data.loc[:,'Sentiment_Type']=sentiment_type 
data.to_csv('Final_Results_FB.csv',index=None)
os.chdir(path)