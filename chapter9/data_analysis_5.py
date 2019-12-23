import pandas as pd
from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，只展现指定结果集
    sql = 'select song_singer from song limit 10'
    result = MySql().read_table(sql)
    return result


def data_deal():
    record_list = get_data()
    df = pd.DataFrame(record_list)
    print('分组前：\n{}'.format(df))
    group_res = df.groupby(['song_singer'])
    print('分组结果：\n{}'.format(group_res.size()))


if __name__ == "__main__":
    data_deal()
