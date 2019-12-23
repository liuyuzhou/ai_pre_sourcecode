from sqlalchemy import create_engine


def get_engine():
    """
    创建engine并返回
    :return: engine 对象
    """
    connect_str = 'mysql+pymysql://root:root@localhost:3306/ai?charset=utf8'
    engine = create_engine(connect_str, echo=False)
    return engine
