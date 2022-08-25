import requests
import json

start = 1
end = 200
step = 200
datalen = 30
url = 'https://api.cafebazaar.ir/rest-v1/process/ReviewRequest'

comments =["id", "date", "versionCode", "rate", "likes", "comment"] 
for i in range(datalen):
    payload = {'properties': {"language": 2, "clientID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "deviceID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "clientVersion": "web"
                              }, 'singleRequest': {"reviewRequest": {"packageName": "cab.snapp.passenger", "start": start, "end": end}}}
    res = requests.post(url, json=payload)
    start = start + step
    end = end + step
    res_json = json.loads(res.text)
    print(res.status_code)
    for j in range(end-start):
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['id']))
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['date']))
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['versionCode']))
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['rate']))
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['likes']))
        comments.append((res_json['singleReply']['reviewReply']['reviews'][j]['comment']))

def removeCamma(text):
    listofcamma = ['،', ',']
    for i in range(len(listofcamma)):
        text = text.replace(listofcamma[i], "") 
    return text
    

for com in range (len(comments)):
    if ((com + 1) % 6 == 0):
        comments[com] =removeCamma(comments[com]) 
    
with open('snapp-comments-lists.py', 'a', encoding="utf-8") as f:
    f.write(str(comments))
print(len(comments))
