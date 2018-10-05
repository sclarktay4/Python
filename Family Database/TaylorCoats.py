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

class FamDB:
	#Function to create table for database
	def __init__(self, db):
		self.conn=sqlite3.connect(db)
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS Family (id INTEGER PRIMARY KEY, name Text, street TEXT,city TEXT, state TEXT, zip INTEGER, email TEXT, phone INTEGER)")
		self.conn.commit()
		
	#Function to insert persons data using name,street,city,state,zip,email,phone
	def insert(self,name,street,city,state,zip,email,phone):
		self.cur.execute("INSERT OR FAIL INTO Family VALUES(NULL,?,?,?,?,?,?,?)",(name,street,city,state,zip,email,phone))
		self.conn.commit()
				
	#Function to display all entries in database
	def view(self):
		self.cur.execute("SELECT * FROM Family")
		rows=self.cur.fetchall()
		return rows

	#Function to delete row in database
	def delete(self,id):
		self.cur.execute("DELETE FROM Family WHERE id=?", (id,))
		self.conn.commit()
		
	#Function to update entry in database
	def update(self,id,name,street,city,state,zip,email,phone):
		self.cur.execute("UPDATE Family SET name=?,street=?, city=?, state=?, zip=?,email=?,phone=? WHERE id=?", (name,street,city,state,zip,email,phone,id))
		self.conn.commit()
		

	#Function to search database using identifing data entered by the user
	def search(self,name="",street="",city="",state="",zip="",email="",phone=""):
		self.cur.execute("SELECT * FROM Family WHERE name=? OR street=? OR city=? OR state=? OR zip=? OR email=? OR phone=?",(name,street,city,state,zip,email,phone))
		rows=self.cur.fetchall()
		return rows
	#Function to deconstruct
	def __del__(self):
		self.conn.close()
		
