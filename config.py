import os

SECRET_KEY = 'teste'

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "insert_password"
MYSQL_DB = "register_people"
MYSQL_PORT = 3306

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'