import requests
from twitter_get_data import query_str
url = "https://graph.facebook.com/v2.10/pages/search"
querystring = {"q":"khaadi","access_token":"EAAG5lfQC6mEBAGdTDTELYF5sCwqwFbZBuNMC0ZBy9QdlZA3mpf2At9JHjXKuUpaI3zZAwHUhwgMY79cMxG4Kj1zRegOjbDQWPzXhOBs9GYGzzNK9BSDQDVe8O1qYcuJN8tolKeKWw8mUFgvGx1vaZAdMOHPYjPd5XLzDZCPhOAxAZDZD"}
headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "a8b12eb1-40db-4114-86fe-5bd0df0a00fb"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
string_response_for_id=response.text


import json
string_json_for_id=json.loads(string_response_for_id)
id_list=[]
try:
    for json_result in string_json_for_id['data']:
        id_list.append(json_result['id'])
except:
    print('Access Token Unavailable;Check Access')

message=[]
created_time=[]
for j in range(0,len(id_list)):
    url = "https://graph.facebook.com/v2.10/"+id_list[j]
    querystring = {"fields":"feed","access_token":"EAAG5lfQC6mEBAGdTDTELYF5sCwqwFbZBuNMC0ZBy9QdlZA3mpf2At9JHjXKuUpaI3zZAwHUhwgMY79cMxG4Kj1zRegOjbDQWPzXhOBs9GYGzzNK9BSDQDVe8O1qYcuJN8tolKeKWw8mUFgvGx1vaZAdMOHPYjPd5XLzDZCPhOAxAZDZD"}
    headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "3021ded9-e2b7-4834-9c3e-0b529f3eef29"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    message_response=response.text
    message_response_json=json.loads(message_response)
    try:
        for rel_data in message_response_json['feed']['data']:
            if(len(rel_data)==4):
                created_time.append(rel_data['created_time'])
                message.append(rel_data['message'])
    except:
        print('Not Found;Access Unavailable')
import os
path=os.getcwd()
os.chdir(query_str)
import pandas as pd
data=pd.DataFrame({'Created_Time':created_time,'Message':message})
data.to_csv('Facebook_Data.csv',index=None,mode='a')
os.chdir(path)
