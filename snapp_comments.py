import requests

start = 1
end = 200
snapp_text = open('snapp_comments2.json', 'a', encoding="utf-8")
url = 'https://api.cafebazaar.ir/rest-v1/process/ReviewRequest'

for i in range(20):
    payload = {'properties' : {"language": 2, "clientID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "deviceID": "hot0ydqh4cw5heubx6gqzkk9y8f8uxfh", "clientVersion": "web"
}, 'singleRequest': {"reviewRequest": {"packageName": "cab.snapp.passenger", "start": start, "end": end} } }
    res = requests.post(url, json = payload)
    start = start + 200
    end = end + 200
    snapp_text.write(res.text)
    print(res.status_code)
snapp_text.close()