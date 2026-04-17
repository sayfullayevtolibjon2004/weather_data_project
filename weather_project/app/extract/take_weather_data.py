import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()
api_key=os.getenv('weather_token')
# print(api_key)

cities = [
    "Andijon", "Bukhara", "Fergana", "Jizzakh", "Urgench", 
    "Namangan", "Navoiy", "Qarshi", "Samarkand", "Guliston", 
    "Termez", "Tashkent", "Nukus"
]

all_weather_data=[]


def take_data():
    try:
        for city in cities:
            
            url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response=requests.get(url)

            if response.status_code==200:
                data=response.json()
                data["weather.description"]=data["weather"][0]["description"]
                data["weather.id"]=data["weather"][0]["id"]
                all_weather_data.append(data)
                #print(f"{city} malumoti olindi")
                
            else:
                print(f"{city} malumotini  olishda xatolik yuz berdi",response.status_code())
        return all_weather_data
    except Exception as e:
        print("sayt bilan bilan bog'lanishda xatolik yoki ip  key  o'zgargan",e)
def create_temporery_table():
    try:
        for city in cities:
            url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response=requests.get(url)
            if response.status_code==200:
                data=response.json()
                folder_path='data/raw'
                file_name = f"{city} -- weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

                full_path=os.path.join(folder_path,file_name)

                with open(full_path,'w') as q:
                    json.dump(data,q,indent=4)
            else:
                print('malumot olishda xatolik yuz berdi',response.status_code())
    except:
            for city in cities:
                url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response=requests.get(url)
                print('malumot olishda xatolik yuz berdi',response.status_code())
