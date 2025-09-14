#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

DB_cfg = {'host':'localhost', 'user':sys.argv[1], 'passwd': sys.argv[2], 'db': sys.argv[3]}

def create_con(DB_cfg):
    try:
        conn = MySQLdb.connect(**DB_cfg)
        return conn
    except MySQLdb.Error as e:
        print(e)
        exit


def do_exe_query(conn, query, args=None):
    c = conn.cursor()
    try:
        c.execute(query, args)
        conn.commit()
    except MySQLdb.Error as e:
        conn.rollback()
        print(e)
    finally:
        c.close()



def do_fetch_query(conn, query, args=None):
    res = None
    c = conn.cursor()
    try:
        c.execute(query, args)
        res = c.fetchall()
        return res
    except MySQLdb.Error as e:
        print(e)
        return None
    finally:
        c.close()

if __name__ == '__main__':
    try:
        conn = create_con(DB_cfg)
        celect_all = "SELECT * FROM states ORDER BY id"
        res = do_fetch_query(conn, celect_all)
        if res != None:
            for i in res:
                print(i)
    finally:
        conn.close()
