"""
@Author: Abid Ebna Saif Utsha
@Date  : 15/03/2020
The color class was taken from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
The api used : https://openweathermap.org/api

city_id = 1185117 - narsingdi
        = 1185241 - dhaka
        = 1733046 - KL
        = 1733037 - selangor
"""
import requests
import json
from datetime import datetime
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def call_weather_api(city,apikey):
    host = 'http://api.openweathermap.org'
    endpoint = f'''/data/2.5/weather?id={city}&appid={apikey}'''
    url = host + endpoint
    header = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.get(url,headers=header)
    respond = response.text
    return respond
def converting_time(pass_time):
    return datetime.fromtimestamp(pass_time)
def processing_weather_information(id):
    apikey = '1f' # hiding my api
    res=json.loads(call_weather_api(id, apikey))
    processing_display(res)

def processing_display(res):
    print(f'''{color.BLUE}coordination:{color.END} {res['coord']}, {color.YELLOW}state:{color.END} {res['name']}, {color.GREEN}country:{color.END} {res['sys']['country']}''')
    print(f'''{color.RED}temparature:{color.END} {round(res['main']['temp']-273,2)}C, {color.RED}feels like:{color.END} {round(res['main']['feels_like']-273,2)}C, {color.RED}minimum temp:{color.END} {round(res['main']['temp_min']-273,2)}C, {color.RED}maximum temp:{color.END} {round(res['main']['temp_max']-273,2)}C''')
    print(f'''{color.DARKCYAN}pressure:{color.END} {res['main']['pressure']}, {color.DARKCYAN}humidity:{color.END} {res['main']['humidity']}, {color.DARKCYAN}visibility:{color.END} {res['visibility']}, {color.CYAN}wind speed:{color.END} {res['wind']['speed']}, {color.CYAN}weather:{color.END} {res['weather'][0]['description']}''')
    print(f'''{color.PURPLE}sunrise(showing current timezone):{color.END} {converting_time(res['sys']['sunrise'])}, {color.PURPLE}sunset(showing current timezone):{color.END} {converting_time(res['sys']['sunset'])}''')

def main():
    dhaka = '1185241'   #city id for calling api
    narsingdi = '1185117'
    kl = '1733046'
    selangor = '1733037'
    processing_weather_information(dhaka)
    print(f'''{color.UNDERLINE}new{color.END}''')
    processing_weather_information(narsingdi)       # my hometown in Bangladesh
    print(f'''{color.UNDERLINE}new{color.END}''')
    processing_weather_information(kl)              
    print(f'''{color.UNDERLINE}new{color.END}''')
    processing_weather_information(selangor)        # I am studying in Malaysia
    
if __name__ == "__main__":
    main()



