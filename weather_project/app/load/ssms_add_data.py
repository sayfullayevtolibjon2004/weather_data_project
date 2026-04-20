from config.connect_ssms import connect,conn
import transform.sort_by_pandas as trnpn
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def add_ssms():
    cursor = connect()
    try:
        cursor.execute('USE Weather')
        query1 = """
            INSERT INTO stg_WeatherTable 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        df = trnpn.sort_weather()
        
        for index, row in df.iterrows():
            params = (
                int(row['id']), 
                row['davlat'], 
                row['shamol tezligi'], 
                row['temperatura'], 
                row['namlik'], 
                row['malumot'], 
                today, 
                row['viloyat nomi']
            )
            cursor.execute(query1, params)
        cursor.execute("execute Yuklash")

        cursor.commit()
        print(f"{len(df)} ta shahar ma'lumoti Staging jadvalga yozildi.")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
print(add_ssms)