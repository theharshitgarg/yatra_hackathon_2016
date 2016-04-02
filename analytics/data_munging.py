import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
print ",",c
c.execute('SELECT * FROM questions_choice')
print c.fetchone()
for i in c:
    print i
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print "ALL", (c.fetchall())

con = sqlite3.connect('db.sqlite3')
with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)

import pandas.io.sql as sql
con = sqlite3.connect('db.sqlite3')
#table = sql.read_frame('select * from questions_choice', con)
#table.to_csv('output.csv')


import sqlite3, sys, zipfile

dbname = sys.argv[1] if len(sys.argv) > 1 else 'testdb.db'

# Open the db and dump all its data into the 'data' buffer
con = sqlite3.connect(dbname)
data = '\n'.join(con.iterdump())
con.close()

# Create a zip file and write add the dump into it as
# a new file
zf = zipfile.ZipFile('dump.zip',
                     mode='w',
                     compression=zipfile.ZIP_DEFLATED)
zf.writestr('dump.sql', data)
zf.close()
