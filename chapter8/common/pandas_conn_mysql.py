"""
Python与mysql的通信模块，使用连接池的方式，可以执行使用多个连接池连接不同的数据库
"""
import pymysql
import pandas as pd
import traceback
from collections import defaultdict
from DBUtils.PooledDB import PooledDB

# 构建全局的数据库连接池
_db_pool = defaultdict()


class MySql(object):
    """MySQL连接对象"""
    def __init__(self, host=None, port=None, db='ai', connect_timeout=1000,
                 min_cached=0, max_cached=1,max_shared=0, max_connections=30):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'
        # 需要连接哪个DB
        self.db = 'ai'
        # 超时时间
        self.connect_timeout = connect_timeout
        # 初始化时，连接池至少创建的空闲的连接，0表示不创建
        self.min_cached = min_cached
        # 连接池空闲的最多连接数，0和None表示没有限制
        self.max_cached = max_cached
        # 连接池允许的最大连接数，0和None表示没有限制
        self.max_connections = max_connections
        # 连接池中最多共享的连接数量，0和None表示全部共享
        self.max_shared = max_shared
        # 区分不同实例数据库连接池需要的名称
        self.pool_key = '{}:{}:{}'.format(str(host), str(port), db)
        _db_pool[self.pool_key] = PooledDB(creator=pymysql, host=self.host,
                                           port=int(self.port), user=self.user,
                                           passwd=self.passwd, db=self.db, charset='utf8',
                                           connect_timeout=self.connect_timeout,
                                           mincached=self.min_cached,
                                           maxcached=self.max_cached,
                                           maxconnections=self.max_connections,
                                           maxshared=self.max_shared)

    def get_conn(self, only_conn=True):
        """从数据库获取一个连接"""
        conn = _db_pool.get(self.pool_key).connection()
        if only_conn:
            return conn
        else:
            cur = conn.cursor()
            return conn, cur

    @staticmethod
    def close(conn=None, cur=None):
        """关闭数据库连接"""
        if cur:
            cur.close()
        if conn:
            conn.close()

    def read_table(self, sql=None):
        """读取表数据，如果传入表名则直接读取表数据，否则按照sql来读"""
        # print('-' * 80)
        conn = _db_pool.get(self.pool_key).connection()
        data = pd.read_sql(sql, conn)
        data.columns = [col.lower().split('.')[-1] for col in data.columns]
        self.close(conn)
        return data

    def df_into_db(self, tb_name, df, each_commit_row=20000):
        """
        将df导入mysql数据库，不需要特别处理日期列，相比oracle还是很方便的.
        注意，这里是以MySQL写的，如果是其他数据库，需要重新实现该方法。
        """
        if len(df) == 0:
            return 1, ''
        # 获取连接
        conn, cur = self.get_conn(only_conn=False)

        # 创建入库的sql
        sql = "insert into {} ({}) values ({}) "
        cols = list(df.columns)
        cols_string = ', '.join(cols)
        num = len(list(df.columns))
        num_string = ','.join(['%s' for i in range(num)])

        sql = sql.format(tb_name, cols_string, num_string)

        # 入库,默认每次最多提交2w条记录
        try:
            df_len = len(df)
            each_cnt = each_commit_row
            for i in range(0, df_len, each_cnt):
                """
                取出子集，全部转成字符串格式，主要是针对数值，df中的
                时间此时肯定是字符串类型。
                处理空值问题，因为刚才转成字符串时，None被转成"None",
                对于原来是NaN的，要转成空字符串。
              """
                df2 = df.iloc[i:i + each_cnt].applymap(lambda s: str(s))
                nan_df = df.notnull()
                df2 = df2.where(nan_df, None)  # 转成空字符串或空值
                # 将df转成list-tuple格式，才能导入数据库
                param = df2.to_records(index=False).tolist()
                cur.executemany(sql, param)
                conn.commit()
            # 正常关闭连接
            self.close(conn, cur)
            return 1, ''
        except:
            error = traceback.format_exc()
            conn.rollback()
            self.close(conn, cur)
            return 0, error

    def db_update(self, sql):
        """执行SQL"""
        conn, cur = self.get_conn(only_conn=False)
        try:
            cur.execute(sql)
            conn.commit()
            cur.close()
            return 1, ''
        except:
            conn.rollback()
            error = traceback.format_exc()
            print(error)
            return 0, error


def conn_try():
    """
    连接测试
    :return:
    """
    # 连接本地mysql
    local = MySql()  # 非加密方式
    result = local.read_table(sql='select * from basic_info limit 20')
    print(result)


if __name__ == "__main__":
    conn_try()
