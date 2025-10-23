from sqlalchemy import create_engine, text

import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host')
port = os.getenv("port")
user = os.getenv('user')
name = os.getenv('name')
password = os.getenv('password')


sqlite_engine = create_engine('sqlite:///Django_py/db.sqlite3.db')
mysql_engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{name}')

with mysql_engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM django_app_articalmodel"))
    print("Записей в таблице:", result.scalar())
