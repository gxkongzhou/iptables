"""
    Used to query and verity  the correctness of data
"""

from mysql.connector import connect, pooling
from datetime import datetime, timedelta, date

host = "150.135.66.35"
port = 3306
auth_plugin = "mysql_native_password"
user = "vicent"
password = "hp@#2548HPL"
database = 'iptables'

dbcongif = {"host": host, "port": port, "user": user, "auth_plugin": auth_plugin, "password": password,
            "database": database}


class dbcontrol(object):
    def __init__(self, *args, **kwargs):
        self.arge = args
        self.kwargs = kwargs

    def __enter__(self):
        return connect(self.arge, self.kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print exc_type,exc_val,exc_tb
        con.close()


querystr = (
    ""
)

# Ip valid date
today = datetime.now().date()

# User query response function
def query(*args,**kwargs):
    with dbcongif(**dbcongif) as con:
        con = connect(**dbcongif)
        cur = con.cursor()
        cur.execute(querystr)
        list = cur.fetchall()





