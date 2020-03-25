import sqlite3
import os
dbpath='data.sqlite'
if not os.path.exists(dbpath):
    conn=sqlite3.connect(dbpath)
    c=conn.cursor()
    c.execute('''
    CREATE TABLE persons
    id INT PRIMARY KEY  NOT NULL,
    name  TEXT   NOT NULL,
    age   INT    NOT  NULL,
    address   CHAR(50),
    salary     REAL);
    
    
    
    
    
    
    ''')
    conn.commit()
    conn.close()
    print('ok')