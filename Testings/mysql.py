import csv

import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "icecrape", charset='utf8')

# lst =['Offset', 'Name', 'PID', 'PPID', 'Thds', 'Hnds', 'Sess', 'Wow64', 'Start', '`Exit`', 'caseid']
# table_name = "test"
# createsqltable = """CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " VARCHAR(250),".join(lst) + " VARCHAR(250))"
cursor = db.cursor()
# cursor.execute(createsqltable)
# db.commit()

cursor.execute("select * from ikman")

res = cursor.fetchall()
with open('D:\output.csv','w') as fw:
    writer = csv.writer(fw)
    writer.writerows(res)

