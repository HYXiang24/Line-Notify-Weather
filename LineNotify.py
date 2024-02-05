import requests
import json


APIKEY = "0102effbcf62dbfc8581c9f46cbc7159"
lon = '121.5319'
lat = '25.0486'
url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&' + 'lon=' + lon +'&appid=' + APIKEY +'&units=metric'
r = requests.get(url)
data = json.loads(r.text)

temp = round(data['main']['temp'],1)
feels_like = round(data['main']['feels_like'], 1)
temp_min = round(data['main']['temp_min'], 1)
temp_max = round(data['main']['temp_max'], 1)

msg = (f"\n地區 {data['name']}\n目前溫度 {temp}\n體感溫度 {feels_like}\n最高溫 {temp_max} \n最低溫 {temp_min}")

url = 'https://notify-api.line.me/api/notify'
token = "OQEjcAIoY4ewNLVB96VmsJl30I9ptgyOpAnnJOEK1aX"
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':msg,     # 設定要發送的訊息
}
data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法
