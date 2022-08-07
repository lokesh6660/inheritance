import mysql connector as c
con= c.connect(host="localhost",
               use="root",
               passwd="lucky",
               database='cetpa')
cursor=con.cursor()
name=input("enter your name:")
dob=input("enter your dob:")
salary=input("enter your salary:")
#query->insert
query="insert into detail values('[]','[]',[])".format(name,dob,salary)
cursor.execute(query)
con.commit()
print("data enter successfully!!")