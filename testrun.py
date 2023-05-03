import mysql.connector
from asterisk.ami import AMIClient 

client = AMIClient(address="54.36.181.102", port=5038)
client.login(username='manager' , secret='im')
                                                  
mydb = mysql.connector.connect(
    host = "54.36.181.102", 
    user = "Jaheim1",
    password = "root",
    database = "UserAsterisk_db"
)

caller_id = "SIP/Admin"
cursor = mydb.cursor()
cursor.execute(f"SELECT CashAmount FROM Accounts WHERE caller_id='{caller_id}'")
result = cursor.fetchone()

if result is not None:
    call_duration = result[0]
else:
    print("You're Broke")
    exit()
    
action = {
    'Action' : 'Originate', 
    'Channel' : 'SIP/Admin',
    'Context' : 'Trial',
    'Exten' : '1234',
    'Priority': '1',
    'SetVar': f'CALL_TIMEOUT={int(call_duration*60)}'
}

response = client.send_action(action)
if response.is_error():
    print(response.get_error())
else:
    print(f"Dialing {action['Channel']} with {int(call_duration*60)} seconds timeout")

# Disconnect from Asterisk Manager Interface
client.logoff()
client.close()

# Close MySQL database connection
mydb.close()


#Cursor Point Connection
# mycursor = mydb.cursor()

# #Read Items in the Table 
# mycursor.execute("SELECT * FROM Accounts")
# myresults = mycursor.fetchall()


# for item in myresults:
#     print(item)
    
    
    
    
        
