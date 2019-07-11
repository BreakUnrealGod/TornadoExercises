from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import mysql

db_url = 'mysql+pymysql://{}:{}@{}:{}/{}'. \
    format(mysql['user'], mysql['password'], mysql['host'], mysql['port'], mysql['dbname'])

# 创建连接
engine = create_engine(db_url)

# 构建Base对象
Base = declarative_base(engine)

# 创建session
Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    con = engine.connect()
    print(con)
