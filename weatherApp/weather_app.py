import requests
import json
import time

city_list = ['mumbai', 
            'kolkata', 
            'delhi', 
            'ambala', 
            'dhanera', 
            'disa', 
            'bengaluru',
            'london',
            'moscow',
            'kathmandu',
            'pune',
            'jaipur',
            'goa',
            'gangtok', 
            'manali', 
            'chandigarh', 
            'surat',
            'nagpur',
            'belgium',
            'Sharjah',
            'dhaka', 
            'bhopal',
            'indore',
            'ujjain',
            'tokyo',
            'paris',
            'jakarta',
            'riva',
            'sagar',
            'jabalpur',
            'gwalior',
            'lucknow',
            'manhatten',
            'arizona',
            'berlin',
            'howrah',
            'boston',
            'kurnool',
            'satna',
            'sidhi',
            'mirzapur',
            'dhanbad',
            'raipur',
            'chapra',
            'bilaspur',
            'mysore',
            'chennai',
            'amritsar',
            'contai',
            'kota',
            'bundi',
            'bhind',
            'jhansi'
            ]

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
weather_data = {}
weather_data['weather'] = []

def read_file():
  with open('weatherApp/weather_data.json','r') as external_file:
    try:
      old_data = json.load(external_file)
    except json.decoder.JSONDecodeError:
      return weather_data
    return old_data

def write_file(data):
  old_data = read_file()
  print('writting data into file.')
  with open('weatherApp/weather_data.json','w') as external_file:
    old_data['weather'].append(data)
    json.dump(old_data, external_file, indent=2)

def get_weather(city):
  url = api_address + city
  print(f'Getting weather report for city : {city}')
  response = requests.get(url)
  response = response.json()
  response['main']['city'] = city
  write_file(response['main'])

def main(cities):
  for city in cities:
    get_weather(city)

if __name__ == '__main__':
    start_time = time.perf_counter()
    main(city_list)
    end_time = time.perf_counter()
    timedelta = end_time - start_time
    print(timedelta)
