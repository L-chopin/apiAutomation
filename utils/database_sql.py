from utils.database_connection_utils import dbc_Utils

class sql:

    @classmethod
    def select_by_id(cls,table):
        connect = dbc_Utils.get_connect()
        cursor = dbc_Utils.get_cursor(connect)

        sql = "SELECT id FROM %s" % table
        cursor.execute(sql)

        return cursor.fetchone[0]

    @classmethod
    def delete_by_id(cls,table,id):
        connect = dbc_Utils.get_connect()
        cursor = dbc_Utils.get_cursor(connect)

        sql = "DELETE FROM %s WHERE id = %s" % (table,id)
        cursor.execute(sql)
        connect.commit()

        return cursor.rowcount
