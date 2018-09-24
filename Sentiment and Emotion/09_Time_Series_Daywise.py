import pandas as pd
from twitter_get_data import query_str
import os
path=os.getcwd()
os.chdir(query_str)

data=pd.read_csv('Final_Results.csv',encoding='ISO-8859-1')
import datetime
for i in range(0,len(data)):
    data.loc[:,'Date'][i]=datetime.datetime.strptime(data.loc[:,'Date'][i],('%Y-%m-%d %H:%M:%S'))

start=datetime.datetime.strptime('2018-01-01',('%Y-%m-%d'))
months=start.month
days=[]
for i in range(0,len(data)):
    days.append((data.loc[:,'Date'][i]-start).days)

x=[0]*7    
for i in days:
    x[i%7]+=1
y=[1,2,3,4,5,6,7]

import matplotlib.pyplot as plt
plt.plot(y,x)
plt.xticks(y,['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
plt.xlabel('Day')
plt.ylabel('Count')
plt.title('Tweets_DayWise')
plt.savefig('Tweets_DayWise.png')
plt.show()

x=[0]*12
for i in days:
    try:
        x[int(i/30)]+=1
    except:
        x[int(i/30)-1]+=1

y=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.scatter(y,x)
plt.xticks(y,['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Tweets_Monthwise')
plt.savefig('Tweets_Monthwise.png')
plt.show()
os.chdir(path)