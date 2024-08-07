import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-082E9804-D1A2-4ECC-AB65-28C550F4A2CA'
r = requests.get(URL, params=P)
t = r.json()

n = len(t['records']['Station'])
for i in range(n):
    print(i,t['records']['Station'][i]['StationName'])

location = input('查詢站點: ')
while location:
    found = False
    for i in range(n):
        if t['records']['Station'][i]['StationName'] == location:
           print('觀測地點: ', t['records']['station'][i]['StationName'])
           print('觀測時間: ', t['records']['station'][i]['ObsTime']['DateTime'])
           print('觀測溫度: ', t['records']['station'][i]['WeatherElment']['AirTemperature'])
           print('觀測濕度: ', t['records']['station'][i]['WeatherElment']['RelativeHumidity'])
           print('觀測天氣: ', t['records']['station'][i]['WeatherElment']['Weather'])
           found=True
           break
    
if (found == False):
    print('輸入站點不存在')

    location = input('查詢站點: ')