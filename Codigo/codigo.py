#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","Teste" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("CREATE DATABASE LOL")

# Create table as per requirement
# sql = "INSERT INTO Numero (numero) VALUES (312)"
# cursor.execute(sql)

# disconnect from server
db.close()