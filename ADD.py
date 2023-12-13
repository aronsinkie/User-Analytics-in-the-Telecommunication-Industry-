import os
import pandas as pd
import psycopg2
from psycopg2 import Error

def DBConnect(dbName=None):
    conn = psycopg2.connect(host='localhost',
                            user='postgres',
                            password='Aron123@aron123@',
                            database=dbName)
    cur = conn.cursor()
    return conn, cur



def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} records fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res

