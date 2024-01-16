import os
from sqlalchemy import create_engine

BASEDIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_PATH = os.path.join(BASEDIR, 'static/assets/blog')
SECRET_KEY = "sdkfjlasdf%$^%^&qjluio23asdfu42903"
#db_path = os.path.join(os.path.dirname(__file__), 'personal.sqlite')
#engine = create_engine('mysql+pymysql://root:phpts@localhost:3306/personal?charset=utf8')
#engine = create_engine('sqlite:///{}'.format(db_path))
#SQLALCHEMY_DATABASE_URI = str(engine.url)
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_ECHO = False



# 设置参数
MYSQL_DIALECT = 'mysql'
MYSQL_DRIVER = 'pymysql'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '12345678'
MYSQL_HOST = '127.0.0.1' # localhost/127.0.0.1
MYSQL_PORT = 3306
MYSQL_DB = 'personal'
MYSQL_CHARSET = 'utf8mb4'
# 数据库链接字符串URI
SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DRIVER}://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
# 数据盐
SECRET_KEY = os.urandom(16)

SQLALCHEMY_COMMIT_ON_TERADOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

PER_PAGE = 10