import mysql.connector
from asterisk.ami import AMIClient, SimpleAction

client = AMIClient(address="54.36.181.102", port=5038)
client.login(username='manager', secret='im')
                                                  
mydb = mysql.connector.connect(
    host = "54.36.181.102", 
    user = "Jaheim1",
    password = "root",
    database = "UserAsterisk_db"
)

def callback_originate(events):
    print(events)

CellphoneID = "SIP/User"
cursor = mydb.cursor()
cursor.execute(f"SELECT CashAmount FROM Accounts WHERE CellphoneID='{CellphoneID}'")
result = cursor.fetchone()

if result is not None:
    balance = result[0]
else:
    print("You're not authrorized to make calls")
    exit()

balance = 4
if balance > 0:
    call_duration = balance / 2
else:
    print("You're broke")
    exit()
    
variables = {
    'CALL_TIMEOUT': int(call_duration*60)
}

action = SimpleAction(
    'Originate', 
    Channel= "SIP/Admin",
    Context= "Trial",
    Exten= '4000',
    variables = variables,
    Priority=1
)

response = client.send_action(action)
# if response.is_error():
#     print(response.get_error())
# else:
#     print(f"Dialing SIP/Admin with {int(call_duration*60)} seconds timeout")


# Disconnect from Asterisk Manager Interface
client.logoff()

# Close MySQL database connection
mydb.close()


#Cursor Point Connection
# mycursor = mydb.cursor()

# #Read Items in the Table 
# mycursor.execute("SELECT * FROM Accounts")
# myresults = mycursor.fetchall()


# for item in myresults:
#     print(item)
    
    
    
    
        
