import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DATETIME

# 声明映射
Base = declarative_base()
# 创建Session
Session = sessionmaker()
# 创建连接引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/ai?charset=utf8', echo=False)
Session.configure(bind=engine)
# 构造新的Session
session = Session()


# 定义Course对象，课程表对象
class BasicInfo(Base):
    # 表的名字
    __tablename__ = 'basic_info'
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, default=0, nullable=False, comment='图片id')
    product_code = Column(String(200), default=None, nullable=False, comment='产品代码')
    create_date = Column(DATETIME, default=datetime.datetime.now(), nullable=False, comment='创建时间')
    update_date = Column(DATETIME, default=None, nullable=True, comment='更改时间')


Base.metadata.create_all(engine)
