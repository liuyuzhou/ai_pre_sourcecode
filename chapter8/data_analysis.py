import pandas as pd
import numpy as np
import matplotlib as mp
from chapter8.pandas_conn_mysql import MySql


def get_data():
    # 连接本地mysql
    sql = 'select * from song'
    result = MySql().read_table(sql)
    # print(result)
    return result


def deal_with_null():
    record_list = get_data()
    rl = pd.DataFrame(record_list)
    # rl.dropna()
    # print(rl.info())
    print(rl['song_singer'].value_counts())
    # for item in record_list:
    #     print('----------------------')
    #     record = pd.Series(item, ['id', 'image_id', 'product_code', 'en_name'])
    #     print(record)


def song_count():
    record_list = get_data()
    rl = pd.DataFrame(record_list)
    # rl.dropna()
    # print(rl.info())
    print(rl['song_singer'].value_counts())


def show_count():
    record_list = get_data()
    rl = pd.DataFrame(record_list)
    # rl.dropna()
    # print(rl.info())
    cframe = rl[rl.song_singer.notnull()]
    cframe['os'] = np.where(cframe['song_singer'].str.contains('o'), 'Windows', 'Not Windows')
    # print(cframe['os'])
    by_tz_os = cframe.groupby(['song_singer', 'os'])
    agg_counts = by_tz_os.size().unstack().fillna(0)
    print(agg_counts[:10])


if __name__ == "__main__":
    # get_data()
    # deal_with_null()
    show_count()

