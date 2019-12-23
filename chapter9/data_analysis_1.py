import numpy as np
import pandas as pd

from numpy import nan as NA

from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 连接本地mysql
    sql = 'select song_ablum from song limit 10'
    result = MySql().read_table(sql)
    # print(result)
    return result


def deal_with_null():
    record_list = get_data()
    rl = pd.DataFrame(record_list)
    rl.dropna()
    print(rl)
    # print(rl.isnull)
    # print(rl['song_singer'].value_counts())
    # # for item in record_list:
    # #     print('----------------------')
    # #     record = pd.Series(item, ['id', 'image_id', 'product_code', 'en_name'])
    # #     print(record)
    # string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
    # print(string_data.isnull())

    # data = pd.Series([1, NA, 3.5, NA, 7])
    # print(data)
    # print(data.dropna())
    print(rl.fillna(0))


if __name__ == "__main__":
    deal_with_null()
