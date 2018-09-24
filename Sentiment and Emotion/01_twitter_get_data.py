import csv
import tweepy
import unidecode

# AUTHENTICATION (OAuth)
#f = open('auth.k','r')
#ak = f.readlines()
#f.close()
auth1 = tweepy.auth.OAuthHandler("4dSRTVHHOW5yAG9SoGde8BQmA", "uPS8rPXRnJ22ywyLT5nOPbhwZewkxSvpoAtMFzRYA7030TJFm4")
auth1.set_access_token("1017059171831726080-bgEr0i0auQvdoegAXp71CfbkYUwjca", "pmaMinQ979U03nmphqDfr0XZGZVUBXPblU7gSiCYHtSCn")
api = tweepy.API(auth1,wait_on_rate_limit=True)

# Twitter search with keyword
target_num = 1000
query = ("khaadi OR lawn") #Your hashtags here separated by OR
global query_str=query.split('OR')[0]
dates="2018-01-01"
dateu="2018-09-02"

import os
if(os.path.isdir(query_str)):
    os.chdir(query_str)
else:
    os.mkdir(query_str)
    
if('emotion_results.csv' in os.listdir()):
    csvFile = open('emotion_results.csv','a+',newline='',encoding='utf8')
else:
    csvFile = open('emotion_results.csv','w+',newline='',encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow([ "Text","Date","Location","Retweet count","User Name","Author ID","Followers","Friends"])
counter = 0

for tweet in tweepy.Cursor(api.search, q = query, lang = "en", result_type = "all",since=dates,until=dateu, count = target_num).items():
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        created = tweet.created_at
        text = tweet.text
        text = unidecode.unidecode(text)
        retwc = tweet.retweet_count
        location= tweet.user.location
        try:
            hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
        except:
            hashtag = "None"
        username  = tweet.author.name            #author/user name
        authorid  = tweet.author.id              #author/user ID#
        followers = tweet.author.followers_count #number of author/user followers (inlink)
        friends = tweet.author.friends_count     #number of author/user friends (outlink)
    
        csvWriter.writerow([text,created,location,retwc,username,authorid,followers,friends])
    
        counter = counter + 1
        if (counter == target_num):
            break
    
csvFile.close()
