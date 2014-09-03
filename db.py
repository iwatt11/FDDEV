#!/usr/local/bin/python2.7
import pymysql
_connection = False

def get_connection():
    global _connection
    if not _connection:
        try :
            _connection = pymysql.connect(db='imdb', user='root', passwd='', host='localhost')
        except pymysql.Error, e :
            print ("Couldn't connect to database. MySQL error %d: %s" %
                   (e.args[0], e.args[1]))
    return _connection

def run_query(query,params):
    cur = _connection.cursor() 
    cur.execute(query,params)
    vals = cur.fetchall()
    cur.close()
    return vals


def close_connection():
    _connection.close()