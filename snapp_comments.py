import requests
import json

start = 1
end = 200
url = 'https://api.cafebazaar.ir/rest-v1/process/ReviewRequest'

comments = ["id", "date", "versionCode", "rate", "likes", "comment"]
for i in range(30):
    payload = {'properties': {"language": 2, "clientID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "deviceID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "clientVersion": "web"
                              }, 'singleRequest': {"reviewRequest": {"packageName": "cab.snapp.passenger", "start": start, "end": end}}}
    res = requests.post(url, json=payload)
    start = start + 200
    end = end + 200
    res_json = json.loads(res.text)
    print(res.status_code)
    for j in range(end-start):
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['id'])
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['date'])
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['versionCode'])
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['rate'])
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['likes'])
        comments.append(res_json['singleReply']['reviewReply']['reviews'][j]['comment'])

with open('comments2.csv', 'a', encoding="utf-8") as f:
    f.write(str(comments))
print(len(comments))