"""
This program stores family information:
Name, Street, City, State, Zip, Email

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close

By: Samuel Taylor
"""
import sqlite3


#Function to create table for database
def create_table():
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Family (id INTEGER PRIMARY KEY, name Text, street TEXT,city TEXT, state TEXT, zip INTEGER, email TEXT, phone INTEGER)")
    conn.commit()
    conn.close

#Function to insert persons data using name,street,city,state,zip,email,phone
def insert(name,street,city,state,zip,email,phone):
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("INSERT OR FAIL INTO Family VALUES(NULL,?,?,?,?,?,?,?)",(name,street,city,state,zip,email,phone))
    conn.commit()
    conn.close

#Function to display all entries in database
def view():
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Family")
    rows=cur.fetchall()
    conn.close
    return rows

#Function to delete row in database
def delete(id):
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Family WHERE id=?", (id,))
    conn.commit()
    conn.close

#Function to update entry in database
def update(id,name,street,city,state,zip,email,phone):
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("UPDATE Family SET name=?,street=?, city=?, state=?, zip=?,email=?,phone=? WHERE id=?", (name,street,city,state,zip,email,phone,id))
    conn.commit()
    conn.close

#Function to search database using identifing data entered by the user
def search(name="",street="",city="",state="",zip="",email="",phone=""):
    conn=sqlite3.connect("Family.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Family WHERE name=? OR street=? OR city=? OR state=? OR zip=? OR email=? OR phone=?",(name,street,city,state,zip,email,phone))
    rows=cur.fetchall()
    conn.close
    return rows
#Main code of program to create table for database
create_table()
