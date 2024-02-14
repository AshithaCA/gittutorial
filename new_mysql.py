import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3307,
    database = 'project'
)
mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# # print(mycursor)
# for x in mycursor:
#     print(x)


#........................insert....................................


# mycursor.execute('create database project')
# mycursor.execute('create table customers(name varchar(255),address varchar(255))')
# sql='insert into customers(name,address) values(%s,%s)'
# val=[
#     ('nitha','lowstreet 4'),
#     ('midhun','apple st 652'),
#     ('gayathri','mountain 21'),
#     ('aishu','main road 989'),
#      ('anjith','sideway 1633')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()

# m="insert into customers(name,address) values('shiny','shiny vila')"
# mycursor.execute(m)
# mydb.commit()

#........................select....................................

mycursor.execute('select * from customers')
# myresult= mycursor.fetchone()
# myresult= mycursor.fetchall()
myresult= mycursor.fetchmany
print(myresult)
print(type(myresult))
