import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Final_Results.csv',encoding='ISO-8859-1')
total_length=len(data)
pos=neg=neu=0
for i in data.loc[:,'Sentiment_Type']:
    if(i=='Positive'):
        pos+=1
    elif(i=='Negative'):
        neg+=1
    else:
        neu+=1

print(str(pos/total_length*100)+'% of positive tweets related to the hashtag')
print(str(neg/total_length*100)+'% of negative tweets related to the hashtag')
print(str(neu/total_length*100)+'% of neutral tweets related to the hashtag')

os.chdir(path)
