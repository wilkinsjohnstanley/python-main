import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
#iterate through all the data to get some in particular
for data in response.json()['items']:
    if data['answer_count']==0:
        print(data['title'])
        print(data['link'])
        print(data['answer_count'])
        print()
    else:
        print("skipped")

