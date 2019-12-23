import pandas as pd
from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，只展现指定结果集
    sql = 'select song_name,song_ablum,song_singer from song limit 6'
    result = MySql().read_table(sql)
    return result


def data_deal():
    record_list = get_data()
    df = pd.DataFrame(record_list)
    pieces = dict(list(df.groupby('song_singer')))
    print('分组迭代结果：\n{}'.format(pieces))


if __name__ == "__main__":
    data_deal()
