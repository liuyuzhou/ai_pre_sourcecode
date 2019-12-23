from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 连接数据库
def get_db_conn_info():
    conn_info_r = "mysql+pymysql://root:root@localhost/ai?charset=UTF8"
    return conn_info_r


# 创建会话对象，用于数据表的操作
conn_info = get_db_conn_info()
engine = create_engine(conn_info, echo=False)

# 创建Session实例
db_session = sessionmaker(bind=engine)
session = db_session()
"""
创建基类实例
declarative_base()是一个工厂函数，为声明性类定义构造基类
"""
BaseModel = declarative_base()


# 映射数据表
class Song(BaseModel):
    # 表名
    __tablename__ ='song'
    # 字段，属性
    id = Column(Integer, primary_key=True)
    song_name = Column(String(50), default=None, nullable=True, comment='歌名')
    song_ablum = Column(String(50), default=None, nullable=True, comment='专辑')
    song_interval = Column(Integer, default=0, nullable=False, comment='时长')
    song_songmid = Column(String(50), default=None, nullable=True, comment='歌曲mid')
    song_singer = Column(String(50), default=None, nullable=True, comment='歌手')
    song_count = Column(Integer, default=0, nullable=False, comment='歌曲数')
    create_time = Column(DATETIME, default=None, nullable=True, comment='创建时间')


# 创建数据表
BaseModel.metadata.create_all(engine)
