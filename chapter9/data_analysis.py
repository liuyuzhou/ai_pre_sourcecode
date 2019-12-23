from chapter9.common.pandas_conn_mysql import MySql


def get_data():
    # 为便于观看结果形式，示例中只输出一条记录
    sql = 'select * from song limit 1'
    result = MySql().read_table(sql)
    print('数据查询结果：\n{}'.format(result))
    return result


if __name__ == "__main__":
    get_data()
