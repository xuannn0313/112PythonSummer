import requests

URL='https://notify-api.line.me/api/notify'
H,P,F={},{},{}
H['Authorization']='Bearer 3dMhDEbEzaee9HSeZ8F7Br11IxI7FomZiG7BIJCS6f4'
P['message']='本機圖片'
F['imageFile']=open('Chiikawa-62820447ac7d4.jpg','rb')
response=requests.post(URL,headers=H,params=P)

