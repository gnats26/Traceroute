import json
import urllib.parse
import requests
import pprint

main_url_api = 'http://freegeoip.net/json/'
# url = main_url_api + urllib.parse.urlencode('moodle.dbit.in')
url = 'http://freegeoip.net/json/moodle.dbit.in'
json_data = requests.get(url).json()
print(json_data)
json_country_name = json_data['country_name']
json_ip = json_data['ip']
json_lat = str(json_data['latitude'])
json_longitude = str(json_data['longitude'])
print(type(json_longitude))
# newip = input("Enter another site \n")
# url1 = 'http://freegeoip.net/json/'+urllib.parse.urlencode(newip)
# json_data = requests.get(url1)
# print(json_data)
print("ip: "+json_ip + "\ncountry: " + json_country_name + "\nLatitude: " + json_lat + "\nLongitude: " + json_longitude)