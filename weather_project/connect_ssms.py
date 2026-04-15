import pyodbc
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# take parol
load_dotenv()

Driver=os.getenv('Driver')
Server=os.getenv('Server')
Database=os.getenv('Database')
uid=os.getenv('uid')
pwd=os.getenv('pwd')

# connecting
def connect():
    try:
        conn1=pyodbc.connect(
        f"Driver={Driver};"
        f"Server=Server;"
        f"Database=Database;"
        f"UID=uid;"
        f"PWD=pwd;"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
        )
        return conn1
    except:
        print("baza bilan bog'lanishda xatolik")
def connect_sqlalchemy():      
    conn2 = create_engine(f"mssql+pyodbc://sa:Salom4592@localhost/{Database}?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes")
    return conn2
    



