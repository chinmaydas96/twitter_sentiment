import pandas as pd
import unicodedata
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Final_Results.csv',encoding='ISO-8859-1')

data['Location']=data['Location'].fillna('Not Available')

for i in range(len(data)):
    try:
        data.loc[:,'Location'][i]=unicodedata.normalize('NFKD', data.loc[:,'Location'][i]).encode('ascii','ignore').strip()
    except:
        data.loc[:,'Location'][i]=data.loc[:,'Location'][i].encode('ascii','ignore').strip()
    if(len(data.loc[:,'Location'][i])==0):
        data.loc[:,'Location'][i]='Not Available'

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['Location']=le.fit_transform(data['Location'])
    
locations=len(le.classes_)
data_pos=[0]*locations
data_neg=[0]*locations
data_neu=[0]*locations
location=['']*locations
for i in range(len(data)):
    location[data.loc[:,'Location'][i]]=str(le.inverse_transform(data.loc[:,'Location'][i]))
    if(data.loc[:,'Sentiment_Type'][i]=='Positive'):
        data_pos[data.loc[:,'Location'][i]]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Negative'):
        data_neg[data.loc[:,'Location'][i]]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Neutral'):
        data_neu[data.loc[:,'Location'][i]]+=1
    
demographic_data=pd.DataFrame({'Location':location,'Positive Tweets':data_pos,'Negative Tweets':data_neg,'Neutral Tweets':data_neu})
demographic_data.to_csv('Demographic_Analysis.csv',index=None)

positive_data_index=sorted(range(len(data_pos)), key=lambda k: data_pos[k])
#Top 5 places with more number of positive tweets
X=[]
y=[]
i=len(positive_data_index)-1
c=i-5
while(i>=c):
    X.append(data.loc[:,'Location'][positive_data_index[i]])
    y.append(data_pos[positive_data_index[i]])
    i-=1

labels_pos=le.inverse_transform(X)
import matplotlib.pyplot as plt
plt.bar(X,y,width=5,align='center')
plt.xticks(X,labels_pos,rotation='vertical')
plt.margins(0.5)
plt.xlabel('Location')
plt.ylabel('Count')
plt.title('Twitter Location Based Positive tweets')
plt.savefig('Positive_Count.png')
plt.show()


negative_data_index=sorted(range(len(data_neg)), key=lambda k: data_neg[k])
#Top 5 places with more number of negative tweets
X=[]
y=[]
i=len(negative_data_index)-1
c=i-5
while(i>=c):
    X.append(data.loc[:,'Location'][negative_data_index[i]])
    y.append(data_neg[negative_data_index[i]])
    i-=1
labels_neg=le.inverse_transform(X)
plt.bar(X,y,width=5,align='center')
plt.xticks(X,labels_neg,rotation='vertical')
plt.margins(0.5)
plt.xlabel('Location')
plt.ylabel('Count')
plt.title('Twitter Location Based Negative tweets')
plt.savefig('Negative_Count.png')
plt.show()



#User Behaviour
le_user=LabelEncoder()
data.loc[:,'Author ID']=le_user.fit_transform(data.loc[:,'Author ID'])
user_happiness=[0]*len(le_user.classes_)
user_sad=[0]*len(le_user.classes_)
user_worry=[0]*len(le_user.classes_)
user_angry=[0]*len(le_user.classes_)
user_relief=[0]*len(le_user.classes_)
user_surprise=[0]*len(le_user.classes_)
user_neutral=[0]*len(le_user.classes_)
user_love=[0]*len(le_user.classes_)
user_hate=[0]*len(le_user.classes_)
user_boredom=[0]*len(le_user.classes_)
user_empty=[0]*len(le_user.classes_)
user_enthusiasm=[0]*len(le_user.classes_)
user_fun=[0]*len(le_user.classes_)

user_name=['']*len(le_user.classes_)
for i in range(len(data)):
    user_name[data.loc[:,'Author ID'][i]]=data.loc[:,'User Name'][i]
    if(data.loc[:,'Emotion_Prediction'][i]=='worry'):
        user_worry[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='sadness'):
        user_sad[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='anger'):
        user_angry[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='happiness'):
        user_happiness[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='relief'):
        user_relief[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='surprise'):
        user_surprise[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='neutral'):
        user_neutral[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='love'):
        user_love[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='hate'):
        user_hate[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='boredom'):
        user_boredom[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='empty'):
        user_empty[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='enthusiasm'):
        user_enthusiasm[data.loc[:,'Author ID'][i]]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='fun'):
        user_fun[data.loc[:,'Author ID'][i]]+=1

data_user=pd.DataFrame({'User Name':user_name,
                        'Tweets_with_worry':user_worry,\
                        'Tweets_with_anger':user_angry,\
                        'Tweets_with_sadness':user_sad,\
                        'Tweets_with_happiness':user_happiness,\
                        'Tweets_with_relief':user_relief,\
                        'Tweets_with_surprise':user_surprise,\
                        'Tweets_with_neutral':user_neutral,\
                        'Tweets_with_love':user_love,\
                        'Tweets_with_hate':user_hate,\
                        'Tweets_with_boredom':user_boredom,\
                        'Tweets_with_empty':user_empty,\
                        'Tweets_with_enthusiasm':user_enthusiasm,\
                        'Tweets_with_fun':user_fun\
                        })
data_user.to_csv('User_Behaviour.csv',index=None)
os.chdir(path)
