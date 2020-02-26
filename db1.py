import mysql.connector
import dns.resolver
db2=mysql.connector.connect(host="localhost",user="root",password="4218",database="dslab")    #connecting to database
cursor=db2.cursor()
cursor.execute('insert into student1 values("varun",4)') #fetching the value from database
cursor.execute('select * from student1')                #inserting data into database
for i in cursor:
    print(i)