import urllib,urllib.request
from urllib.request import Request, urlopen
import json
import requests
import urllib.request as request
import time

DistrictID = 446  # Get your state and district ID here: https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2#/Metadata%20APIs/districts
Date = "24-05-2021"  # Should be only in DD-MM-YYYY format
while True:
	req = urllib.request.Request('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=%s&date=%s' % (DistrictID, Date), headers={'User-Agent': 'Mozilla/5.0'})
	response = urllib.request.urlopen(req)
	data = json.loads(response.read().decode())
	if len(data['sessions']) > 0:
		count =  0
		dose = 0
		length = len(data['sessions'])
		for i in range(length):
			if data['sessions'][i]['available_capacity'] > 0:

				doses = data['sessions'][i]['available_capacity']
				dose += doses

				age = data['sessions'][i]['min_age_limit']
				if age == 45:
					count+=1
		url = 'https://maker.ifttt.com/trigger/event_name_here/with/key/your_IFTTT_webhook_key_here'
		myobj = {'value1': '%s Vaccine centers and %s Slots Available for age 45+' % (count, dose)}
		x = requests.post(url, data = myobj)
		print(x.text)
	else:
		print("No Slots Available")
	time.sleep(20)
