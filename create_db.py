#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import sys
conn = sqlite3.connect('1.db')
flh = open('db/db.csv','r')
c = conn.cursor()
c.execute('''CREATE TABLE bssids  (bssid text, lat text, lon text)''')
cnt =0  
for line in flh :
    cnt+=1
    arr = line.strip().split("\t")
    c.execute("INSERT INTO bssids VALUES ('{}','{}','{}')".format(arr[0],arr[1],arr[2]))
    if (cnt % 100000 == 0):
    	conn.commit()
flh.close()
sql_index= """CREATE UNIQUE INDEX bssid_index on bssids (bssid);"""
c.execute(sql_index)
conn.close()
