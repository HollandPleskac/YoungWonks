import sqlite3
conn=sqlite3.connect('example.db')

#conn.cursor() is needed to make any operation with the database statement
c=conn.cursor()

#.execute() is used to execute an SQL statement
##c.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)')
name1="Vishal"
phone1="855-987-2342"
email1="vishal@gmail.com"
password1 = "123"

name2="Richard"
phone2="510-123-3456"
email2="richard@gmail.com"
password2="456"

#if you need python variables u have to use ? marks as place holders
c.execute("INSERT INTO users( name, phone, email, password) \
          VALUES(?,?,?,?,)", (name1,phone1,email1,password1))

c.execute("INSERT INTO users( name, phone, email, password) \
          VALUES(?,?,?,?,)", (name2,phone2,email2,password2))
print('users inserted')

# DROP is delete
##c.execute('DROP TABLE users')

#conn.commit() is needed to commit changes 
conn.commit()

#closes the connection to the database
conn.close()
