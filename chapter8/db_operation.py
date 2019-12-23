import pandas as pd
from chapter8.common.pandas_conn_mysql import MySql


def db_insert():
    """
    从csv读取数据插入数据表
    :return:
    """
    # 连接本地mysql
    conn = MySql()
    # 为便于操作数据查看，此处设置插入5条记录
    df = pd.read_csv('files/basic_info_1.csv', nrows=5)
    conn.df_into_db('basic_info', df)
    print('数据插入成功。')


def db_update():
    """
    表记录更新
    :return:
    """
    # 连接本地mysql
    conn = MySql()
    # 将 id 为 2 的记录的 image_id 值更改为 123456
    update_sql = 'update basic_info set image_id={} WHERE id={}'.format(123456, 2)
    conn.db_update(update_sql)
    print('数据更新成功。')


def db_query():
    """
    表记录查询
    :return:
    """
    # 连接本地mysql
    conn = MySql()
    query_sql = 'select * from basic_info'
    query_result = conn.read_table(query_sql)
    print('表记录查询结果：\n{}'.format(query_result))


if __name__ == "__main__":
    # db_insert()
    db_update()
    db_query()
