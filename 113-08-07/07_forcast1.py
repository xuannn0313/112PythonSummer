import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063'
P = {}
P['Authorization'] = 'CWA-082E9804-D1A2-4ECC-AB65-28C550F4A2CA'
r = requests.get(URL, params=P)
t = r.json()

n =len(t['records'['iocations']][0]['iocation'])
for i in range(n):
    print(i,t['records'['iocations']][0]['iocation'][i]['locationName'])