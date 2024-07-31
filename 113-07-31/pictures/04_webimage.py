import requests

IMG='https://th.bing.com/th/id/OIP.sc1x5nZvNVq1vJlp3a_I1wHaD5?rs=1&pid=ImgDetMain'
URL='https://notify-api.line.me/api/notify'
H,P,F={},{},{}
H['Authorization']='Bearer 3dMhDEbEzaee9HSeZ8F7Br11IxI7FomZiG7BIJCS6f4'
P['message']='網路圖片'
F['imageFile']= requests.get(IMG).content
response=requests.post(URL,headers=H,params=P,files=F)

print(response.status_code)
print(response.text)
