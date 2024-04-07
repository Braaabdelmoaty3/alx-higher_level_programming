import mysql.connector 
import MySQLdb

connect = MySQLdb.connect(
        host="localhost", user="name", passwd="pas", db="database", port=3306
    )
mycursor = mysql.cursor()
print("cOnnect")
