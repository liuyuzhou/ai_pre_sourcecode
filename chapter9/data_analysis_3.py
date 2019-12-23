import pandas as pd
from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，只展现指定结果集
    sql = 'select song_ablum,song_singer from song limit 8'
    result = MySql().read_table(sql)
    return result


def data_deal():
    record_list = get_data()
    df = pd.DataFrame(record_list)
    print('数据替换前：\n{}'.format(df))
    # 传递一个替换列表进行数据替换
    rp_data = df.replace(['Post Life Crisis', 'Gozzard'], ['test', 'replace'])
    print('数据替换后：\n{}'.format(rp_data))


if __name__ == "__main__":
    data_deal()
