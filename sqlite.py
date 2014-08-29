#!/usr/bin/env python
import sqlite3
DATABASE = "unko"

def sql4execute(sql,params=[]):
    db = sqlite3.connect(DATABASE)
    db.text_factory = str
    cur = db.execute(sql,params)
    db.commit()
    db.close()

sql = "insert into unko (a)  values ('0001')"
sql4execute(sql)

