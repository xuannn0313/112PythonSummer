import requests

URL='https://notify-api.line.me/api/notify'
H, P={},{}
H['Authorization']='Bearer 3dMhDEbEzaee9HSeZ8F7Br11IxI7FomZiG7BIJCS6f4'
P['message']='貼圖測試'
P['stickerPackageId']=8515
P['stickerId']=16581243
response=requests.post(URL,headers=H,params=P)

print(response.status_code)
print(response.text)