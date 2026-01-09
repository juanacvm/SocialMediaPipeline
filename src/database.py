from config import db_driver, server, db_name, user, password
from sqlalchemy import create_engine 
import urllib


param = (
        f"DRIVER={{{db_driver}}};"
        f"SERVER={server};"
        f"DATABASE={db_name};"
        f"UID={user};"
        f"PWD={password};"
        "TrustServerCertificate=yes;"
    )

connection_string = urllib.parse.quote_plus(param)

url = f"mssql+pyodbc:///?odbc_connect={connection_string}"

engine = create_engine(url,fast_executemany=True)