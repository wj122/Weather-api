import requests

s_city = "Moscow,RU"
appid = "292cfae3d8acd5ed024c777db045f3d7"
city_id = 524901

res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
    params = {'id': city_id,
            'APPID': appid,
            'units': 'metric',
            'lang': 'ru'})

data = res.json()
time_sec = data['list'][0]['dt']
time_sec_day = time_sec % 86400
time_hrs = time_sec_day//3600

j = 8
j = j - (18 - time_hrs) // 3

min_press = 100000
chet = 0
sum_temp = 0

for i in data['list']:
    if j % 8 == 0 or j % 8 == 1:
        #print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        sum_temp += i['main']['temp']
        chet += 1
    if min_press > i['main']['pressure']:
        min_press = i['main']['pressure']
    j += 1

avg_temp = sum_temp / chet
print('Avarage temp: ', round(avg_temp,2))
print('Min Pressure: ', min_press)
