from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host')
port = os.getenv("port")
user = os.getenv('user')
name = os.getenv('name')
password = os.getenv('password')

sqlite_engine = create_engine('sqlite:///Django_py/db.sqlite3')
mysql_engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{name}')

metadata = MetaData()
metadata.reflect(bind=sqlite_engine)

SqLitesession = sessionmaker(bind=sqlite_engine)
MySQLSession = sessionmaker(bind=mysql_engine)

sqlite_session = SqLitesession()
mysql_session = MySQLSession()

#ИСКЛЮЧЕНИЕ СИСТЕМНЫХ ФАЙЛОВ
SKIP_TABLES = [
    'auth_group', 'auth_group_permissions', 'auth_permission', 
    'auth_user', 'auth_user_groups', 'auth_user_user_permissions',
    'django_admin_log', 'django_content_type', 'django_migrations',
    'django_session', 'django_site'
]

for table_name, table in metadata.tables.items():
    if table_name in SKIP_TABLES:
        continue
#------------------------------------------------------------------------------------------------------------
    rows = sqlite_session.query(table).all()
    if not rows:
        continue

    table.metadata = MetaData()
    table.metadata.create_all(mysql_engine, tables=[table])

    data_to_insert = [dict(row._mapping) for row in rows]
    mysql_table = Table(table_name, MetaData(), autoload_with=mysql_engine)

    mysql_session.execute(mysql_table.insert(), data_to_insert)
    mysql_session.commit()

print("Перенос данных завершен...")
sqlite_session.close()
mysql_session.close()
