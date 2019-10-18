import os

db_host = os.environ.get('DB_HOST', default='localhost')
db_port = os.environ.get('DB_PORT', default='5432')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='notes')
db_password = os.environ.get('DB_PASSWORD', default='')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL = f'postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

