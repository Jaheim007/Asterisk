import mysql.connector

def mysqlconnector():
    try:                                                                         
        mydb = mysql.connector.connect(
            host = "54.36.181.102", 
            user = "Jaheim1",
            password = "root",
            database = "UserAsterisk_db"
        )

        #Cursor Point Connection
        mycursor = mydb.cursor()

        #Read Items in the Table 
        mycursor.execute("SELECT * FROM Accounts")
        myresults = mycursor.fetchall()

        
        for item in myresults:
            print(item)

    except Exception as e:
        print(e)
    
print(mysqlconnector())
    
    
    
        
