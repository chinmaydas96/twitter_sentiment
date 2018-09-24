import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Final_Results.csv',encoding='ISO-8859-1')
import datetime
for i in range(0,len(data)):
    data.loc[:,'Date'][i]=datetime.datetime.strptime(data.loc[:,'Date'][i],('%Y-%m-%d %H:%M:%S'))

start=min(data.loc[:,'Date'])
months=start.month

data_pos=[0]*7    
data_neg=[0]*7    
data_neu=[0]*7    
data_happiness=[0]*7  
data_sad=[0]*7  
data_worry=[0]*7  
data_angry=[0]*7  
data_relief=[0]*7  
data_surprise=[0]*7  
data_neutral=[0]*7  
data_love=[0]*7  
data_hate=[0]*7  
data_boredom=[0]*7  
data_empty=[0]*7  
data_enthusiasm=[0]*7  
data_fun=[0]*7  
y=[1,2,3,4,5,6,7]
for i in range(0,len(data)):
    if(data.loc[:,'Sentiment_Type'][i]=='Positive'):
        data_pos[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Negative'):
        data_neg[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Neutral'):
        data_neu[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='worry'):
        data_worry[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='sadness'):
        data_sad[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='anger'):
        data_angry[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='happiness'):
        data_happiness[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='relief'):
        data_relief[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='surprise'):
        data_surprise[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='neutral'):
        data_neutral[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='love'):
        data_love[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='hate'):
        data_hate[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='boredom'):
        data_boredom[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='empty'):
        data_empty[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='enthusiasm'):
        data_enthusiasm[((data.loc[:,'Date'][i]-start).days)%7]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='fun'):
        data_fun[((data.loc[:,'Date'][i]-start).days)%7]+=1
    
import matplotlib.pyplot as plt
if(not all(v == 0 for v in data_pos)):
    plt.plot(y,data_pos)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Positive_Tweets_Daywise')
    plt.savefig('Positive_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_neg)):
    plt.plot(y,data_neg)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Negative_Tweets_Daywise')
    plt.savefig('Negative_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_neu)):
    plt.plot(y,data_neu)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Neutral_Tweets_Daywise')
    plt.savefig('Neutral_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_worry)):
    plt.plot(y,data_worry)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Worry_Tweets_Daywise')
    plt.savefig('Worry_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_angry)):
    plt.plot(y,data_angry)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Angry_Tweets_Daywise')
    plt.savefig('Angry_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_sad)):
    plt.plot(y,data_sad)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Sad_Tweets_Daywise')
    plt.savefig('Sad_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_happiness)):
    plt.plot(y,data_happiness)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Happiness_Tweets_Daywise')
    plt.savefig('Happiness_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_love)):
    plt.plot(y,data_love)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Love_Tweets_Daywise')
    plt.savefig('Love_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_hate)):
    plt.plot(y,data_hate)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Hate_Tweets_Daywise')
    plt.savefig('Hate_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_relief)):
    plt.plot(y,data_relief)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Relief_Tweets_Daywise')
    plt.savefig('Relief_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_surprise)):
    plt.plot(y,data_surprise)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Surprise_Tweets_Daywise')
    plt.savefig('Surprise_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_boredom)):
    plt.plot(y,data_boredom)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Boredom_Tweets_Daywise')
    plt.savefig('Boredom_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_empty)):
    plt.plot(y,data_empty)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('')
    plt.savefig('Empty_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_neutral)):
    plt.plot(y,data_neutral)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Neu_Tweets_Daywise')
    plt.savefig('Neu_Tweets_Daywise.png')
    plt.show()
    
if(not all(v == 0 for v in data_enthusiasm)):
    plt.plot(y,data_enthusiasm)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Enthusiasm_Tweets_Daywise')
    plt.savefig('Enthusiasm_Tweets_Daywise.png')
    plt.show()

if(not all(v == 0 for v in data_fun)):
    plt.plot(y,data_fun)
    plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
    plt.xlabel('Day')
    plt.ylabel('Count')
    plt.title('Fun_Tweets_Daywise')
    plt.savefig('Fun_Tweets_Daywise.png')
    plt.show()


#Month Wise
data_pos=[0]*12    
data_neg=[0]*12   
data_neu=[0]*12   
data_happiness=[0]*12  
data_sad=[0]*12
data_worry=[0]*12  
data_angry=[0]*12  
data_relief=[0]*12  
data_surprise=[0]*12  
data_neutral=[0]*12 
data_love=[0]*12
data_hate=[0]*12 
data_boredom=[0]*12  
data_empty=[0]*12 
data_enthusiasm=[0]*12  
data_fun=[0]*12

for i in range(len(data)):
    if(data.loc[:,'Sentiment_Type'][i]=='Positive'):
        data_pos[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Negative'):
        data_neg[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Sentiment_Type'][i]=='Neutral'):
        data_neu[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='worry'):
        data_worry[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='sadness'):
        data_sad[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='anger'):
        data_angry[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='happiness'):
        data_happiness[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='relief'):
        data_relief[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='surprise'):
        data_surprise[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='neutral'):
        data_neutral[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='love'):
        data_love[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='hate'):
        data_hate[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='boredom'):
        data_boredom[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='empty'):
        data_empty[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='enthusiasm'):
        data_enthusiasm[(data.loc[:,'Date'][i]).month-1]+=1
    if(data.loc[:,'Emotion_Prediction'][i]=='fun'):
        data_fun[(data.loc[:,'Date'][i]).month-1]+=1
    
y=[1,2,3,4,5,6,7,8,9,10,11,12]

if(not all(v == 0 for v in data_pos)):
    plt.plot(y,data_pos)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Positive_Tweets_Monthwise')
    plt.savefig('Positive_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_neg)):
    plt.plot(y,data_neg)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Negative_Tweets_Monthwise')
    plt.savefig('Negative_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_neu)):
    plt.plot(y,data_neu)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Neutral_Tweets_Monthwise')
    plt.savefig('Neutral_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_worry)):
    plt.plot(y,data_worry)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Worry_Tweets_Monthwise')
    plt.savefig('Worry_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_angry)):
    plt.plot(y,data_angry)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Angry_Tweets_Monthwise')
    plt.savefig('Angry_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_sad)):
    plt.plot(y,data_sad)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Sad_Tweets_Monthwise')
    plt.savefig('Sad_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_happiness)):
    plt.plot(y,data_happiness)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Happiness_Tweets_Monthwise')
    plt.savefig('Happiness_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_love)):
    plt.plot(y,data_love)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Love_Tweets_Monthwise')
    plt.savefig('Love_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_hate)):
    plt.plot(y,data_hate)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Hate_Tweets_Monthwise')
    plt.savefig('Hate_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_relief)):
    plt.plot(y,data_relief)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Relief_Tweets_Monthwise')
    plt.savefig('Relief_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_surprise)):
    plt.plot(y,data_surprise)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Surprise_Tweets_Monthwise')
    plt.savefig('Surprise_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_boredom)):
    plt.plot(y,data_boredom)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Boredom_Tweets_Monthwise')
    plt.savefig('Boredom_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_empty)):
    plt.plot(y,data_empty)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Empty_Tweets_Monthwise')
    plt.savefig('Empty_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_neutral)):
    plt.plot(y,data_neutral)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Neu_Tweets_Monthwise')
    plt.savefig('Neu_Tweets_Monthwise.png')
    plt.show()
    
if(not all(v == 0 for v in data_enthusiasm)):
    plt.plot(y,data_enthusiasm)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Enthusiasm_Tweets_Monthwise')
    plt.savefig('Enthusiasm_Tweets_Monthwise.png')
    plt.show()

if(not all(v == 0 for v in data_fun)):
    plt.plot(y,data_fun)
    plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Fun_Tweets_Monthwise')
    plt.savefig('Fun_Tweets_Monthwise.png')
    plt.show()

os.chdir(path)