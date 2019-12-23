import pandas as pd
import matplotlib.pyplot as plt
from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，只展现指定结果集
    sql = 'select song_name,song_ablum,song_singer,song_interval from song limit 10'
    result = MySql().read_table(sql)
    return result


def data_deal():
    record_list = get_data()
    df = pd.DataFrame(record_list)
    group_res = df.groupby('song_singer')['song_interval']
    avg = group_res.sum()
    # 取得索引列转为list集合
    name_list = list(avg.index)
    # 取得值列转为list集合
    num_list = list(avg.values)
    # 设置 x 轴标签
    plt.xlabel('song_singer')
    # 设置 y 轴标签
    plt.ylabel('song_interval')
    # 设置标题
    plt.title('singer total song interval')
    plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
    plt.show()


if __name__ == "__main__":
    data_deal()
