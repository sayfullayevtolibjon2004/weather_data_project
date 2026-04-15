import take_weather_data
import pandas as pd

# print(take_weather_data.take_data())
def sort_weather():

    df1=pd.json_normalize(take_weather_data.take_data())
    sort_df=df1[["weather.id","sys.country","name","wind.speed","main.temp","main.humidity","weather.description"]]
    replace_names=sort_df.rename(columns={
        'weather.id':'id',
        'sys.country':'davlat',
        'name':'viloyat nomi',
        'wind.speed':'shamol tezligi',
        'main.temp':'temperatura',
        "main.humidity":'namlik',
        'weather.description':'malumot',
        })
    return replace_names


