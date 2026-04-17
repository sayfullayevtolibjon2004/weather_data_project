import extract.take_weather_data as extkwrdt
import pandas as pd

data=extkwrdt.take_data()
def sort_weather():
 
    df=pd.json_normalize(data)
    df_exploded=df.explode('weather')
    sort_df=df_exploded[["weather.id","sys.country","name","wind.speed","main.temp","main.humidity","weather.description"]]
    sort_df.columns=['id','davlat','viloyat nomi','shamol tezligi',"temperatura","namlik","malumot"]
    return sort_df


# print(sort_weather())