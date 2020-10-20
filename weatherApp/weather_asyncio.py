import requests
import time
import asyncio
import aiohttp

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

async def write_file(city, data):
  file_name = f"weatherApp/data/{city}.txt"
  print(f'Writting data for city : {city}')
  with open(file_name,'wb') as f:
      f.write(data)

async def get_weather(city):
  url = api_address + city
  print(f'Getting weather report for city : {city}')
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
        content = await resp.read()
        return content

async def scrap_task(city):
    content = await get_weather(city)
    await write_file(city, content)


async def main(cities):
    tasks = []
    for city in cities:
        tasks.append(scrap_task(city))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main(city_list))
    end_time = time.perf_counter()
    timedelta = end_time - start_time
    print(timedelta)
