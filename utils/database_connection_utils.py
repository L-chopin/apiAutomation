"""
 实现封装：
    连接数据中台测试库
"""
import pymysql

class dbc_Utils:

    # 工具函数：1.获取数据中台测试库连接
    @classmethod
    def get_connect(cls):
        return pymysql.connect(
            host="14.23.109.84",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="Ms77897854",
            charset="utf8"
        )

    # 工具函数：2.获取游标
    @classmethod
    def get_cursor(cls,connect):
        return connect.cursor()

    # 工具函数：3.释放资源
    @classmethod
    def close_resource(cls,cursor,connect):
        if cursor:
            cursor.close()
        if connect:
            connect.close()