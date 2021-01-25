import requests
#city_id= 524901 Moscow

s_city = "Moscow,RU"
city_id = 0
appid = "292cfae3d8acd5ed024c777db045f3d7"
city_id= 524901
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                       params={'id': city_id,
                               'units': 'metric',
                               #'cnt': '5',
                               'lang': 'ru',
                               'APPID': appid})
    data = res.json()
    print(data)
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])

except Exception as e:
    print("Exception (find):", e)
    pass

