import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Final_Results_FB.csv',encoding='ISO-8859-1')
data_pos=0
data_neg=0
data_neu=0
data_happiness=0
data_sad=0
data_worry=0
data_angry=0
data_relief=0
data_surprise=0
data_neutral=0
data_love=0
data_hate=0
data_boredom=0
data_empty=0
data_enthusiasm=0
data_fun=0

for i in range(len(data)):
    if(data.loc[:,'Sentiment_Type'][i]=='Positive'):
        data_pos+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Negative'):
        data_neg+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Neutral'):
        data_neu+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='worry'):
        data_worry+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='sadness'):
        data_sad+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='anger'):
        data_angry+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='happiness'):
        data_happiness+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='relief'):
        data_relief+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='surprise'):
        data_surprise+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='neutral'):
        data_neutral+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='love'):
        data_love+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='hate'):
        data_hate+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='boredom'):
        data_boredom+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='empty'):
        data_empty+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='enthusiasm'):
        data_enthusiasm+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='fun'):
        data_fun+=1
    

total_length=len(data)
print(str(data_pos/total_length*100)+'% of positive tweets related to the hashtag') 
print(str(data_neg/total_length*100)+'% of negative tweets related to the hashtag') 
print(str(data_neu/total_length*100)+'% of neutral tweets related to the hashtag') 

print(str(data_worry/total_length*100)+'% of "worry" tweets related to the hashtag') 
print(str(data_sad/total_length*100)+'% of "sad" tweets related to the hashtag') 
print(str(data_angry/total_length*100)+'% of "angry" tweets related to the hashtag') 
print(str(data_happiness/total_length*100)+'% of "happiness" tweets related to the hashtag') 
print(str(data_relief/total_length*100)+'% of "relief" tweets related to the hashtag') 
print(str(data_surprise/total_length*100)+'% of "surprise" tweets related to the hashtag') 
print(str(data_neutral/total_length*100)+'% of "neutral" tweets related to the hashtag') 
print(str(data_love/total_length*100)+'% of "love" tweets related to the hashtag') 
print(str(data_hate/total_length*100)+'% of "hate" tweets related to the hashtag') 
print(str(data_boredom/total_length*100)+'% of "boredom" tweets related to the hashtag') 
print(str(data_empty/total_length*100)+'% of "empty" tweets related to the hashtag') 
print(str(data_enthusiasm/total_length*100)+'% of "enthusiasm" tweets related to the hashtag') 
print(str(data_fun/total_length*100)+'% of "fun" tweets related to the hashtag') 



import numpy as np                                                               
import matplotlib.pyplot as plt
top=[('Positive',data_pos),('Negative',data_neg),('Neutral',data_neu)]
labels, ys = zip(*top)
xs = np.arange(len(labels)) 
width = 1
plt.bar(xs, ys)
plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)
plt.savefig('FB_Visualiztion_Sentiment.png')
plt.show()

top=[('Worry',data_worry),('Sad',data_sad),('Angry',data_angry),\
     ('Happy',data_happiness),('Sad',data_sad),('Boredom',data_boredom)\
     ,('Empty',data_empty),('Enthusiasm',data_enthusiasm),('Fun',data_fun)\
     ,('Surprise',data_surprise),('Relief',data_relief),('Hate',data_hate),('Love',data_love)]
labels, ys = zip(*top)
xs = np.arange(len(labels)) 
width = 1
plt.bar(xs, ys)
plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)
plt.savefig('FB_Visualiztion_Emotion.png')
plt.show()
os.chdir(path)