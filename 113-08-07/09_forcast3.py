import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063'
P = {}
P['Authorization'] = 'CWA-082E9804-D1A2-4ECC-AB65-28C550F4A2CA'
r = requests.get(URL, params=P)
t = r.json()

n = len(t['records']['locations'][0]['location'])
for i in range(n):
    print(t['records']['locations'][0]['location'][i]['locationName'], 
          t['records']['locations'][0]['location'][i]['weatherElement'][1]['time'][1]['elementValue'][0]['value'])