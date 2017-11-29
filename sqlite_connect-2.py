""" pc info  is a data storage program that writes the data into a database
    auther:william kaiga
    version 0.1
"""
import sqlite3
from ePc_info import Pc_info

conn = sqlite3.connect('pc_info.db')

c = conn.cursor()

c.execute("""CREATE TABLE pcs (
            first text,
            last text,
            model integer
            )""")


def insert_username(username):
    with conn:
        c.execute("INSERT INTO pcs VALUES (:first, :last, :model)", {'first': username.first, 'last': username.last, 'model': username.model})


def get_pcz_by_name(lastname):
    c.execute("SELECT * FROM pcs WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_model(username, model):
    with conn:
        c.execute("""UPDATE pcs SET model = :model
                    WHERE first = :first AND last = :last""",
                  {'first': username.first, 'last': username.last, 'model': model})


def remove_username(username):
    with conn:
        c.execute("DELETE from pcs WHERE first = :first AND last = :last",
                  {'first': username.first, 'last': username.last})

username_1 = Pc_info('Noris', 'abaho', 360)
username_2 = Pc_info('Wangolo', 'joel', 390)

insert_username(username_1)
insert_username(username_2)

pcz = get_pcz_by_name('abaho')
print(pcz)

update_model(username_2, 3010)
remove_username(username_1)

pcz = get_pcz_by_name('joel')
print(pcz)

conn.close()

