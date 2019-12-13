import requests
import json

BASE_URL = "https://timesofindia.indiatimes.com/feeds/feedurllist4.cms?ts=1548996873000&platform=android&feedtype=sjson&andver=533"

response = requests.get(BASE_URL)

data = response.json()
#print (response)
print (data)
print (json.dumps(response.json(), indent=4))

#print (response.json()['home'])
print ("Available tabs for app is:- ")
for hm in data['home']:
    print (hm['name'])
    try:
         print ("URL is :- ", hm['defaulturl'])

    except KeyError:
        print ("Default URL not available for: ", hm['name'])


print ("Available left navigation options for app is:- ")
for nav in data['items']:
    print (nav['name'])
    try:
         URL = nav['defaulturl']
         print (URL)

    except KeyError:
         print ("Default URL not available for: ", nav['name'])