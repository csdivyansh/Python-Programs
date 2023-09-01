import mysql.connector
con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='bank')
print(con)
con.close()
