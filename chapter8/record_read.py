import pandas as pd
from sqlalchemy import create_engine
from chapter8.common.engine_create import get_engine


def db_read():
    try:
        connect_str = 'mysql+pymysql://root:root@localhost:3306/ai?charset=utf8'
        engine = create_engine(connect_str, echo=False)
        read_result = pd.read_sql('select * from basic_info', engine)
        print('表记录查询结果：\n{}'.format(read_result))
    except Exception as ex:
        print(ex)


def db_query():
    try:
        engine = get_engine()
        read_result = pd.read_sql('select * from basic_info', engine)
        print('表记录查询结果：\n{}'.format(read_result))
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    # db_read()
    db_query()
