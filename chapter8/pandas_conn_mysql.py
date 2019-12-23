"""
Python与mysql的通信模块，使用连接池的方式，可以执行使用多个连接池连接不同的数据库
"""
import pymysql
import pandas as pd
from collections import defaultdict
from DBUtils.PooledDB import PooledDB

# 构建全局的数据库连接池
_db_pool = defaultdict()


class MySql(object):
    """MySQL连接对象"""
    def __init__(self, host=None, port=None, db='AI', connect_timeout=28800, min_cached=0, max_cached=1,
                 max_shared=0, max_connections=30):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'
        # 需要连接哪个DB
        self.db = 'music'
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
        self.pool_key = '{}:{}:{}'.format(str(host), str(port), db)  # 区分不同实例数据库连接池需要的名称
        _db_pool[self.pool_key] = PooledDB(creator=pymysql, host=self.host, port=int(self.port), user=self.user,
                                           passwd=self.passwd, db=self.db, charset='utf8',
                                           connect_timeout=self.connect_timeout, mincached=self.min_cached,
                                           maxcached=self.max_cached, maxconnections=self.max_connections,
                                           maxshared=self.max_shared)

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


def main():
    # 连接本地mysql
    local = MySql()  # 非加密方式
    result = local.read_table(sql='select * from song limit 20')
    print(result)


if __name__ == "__main__":
    main()
