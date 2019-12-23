import pandas as pd
import datetime
from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，只展现指定结果集
    sql = 'select song_singer,create_time from song limit 3'
    result = MySql().read_table(sql)
    return result


def data_deal():
    record_list = get_data()
    df = pd.DataFrame(record_list)
    print('填充前：\n{}'.format(df))
    res_rt = df.fillna(datetime.datetime.now())
    print('填充后：\n{}'.format(res_rt))


if __name__ == "__main__":
    data_deal()
