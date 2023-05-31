import mysql.connector
from asterisk.ami import AMIClient

ami = AMIClient(address="54.36.181.102", port=5038)
ami.login(username='manager', secret='im')

                                               
mydb = mysql.connector.connect(
    host = "54.36.181.102", 
    user = "Jaheim1",
    password = "root",
    database = "UserAsterisk_db"
)

CellphoneID = "SIP/User"
cursor = mydb.cursor()
cursor.execute(f"SELECT CashAmount FROM Accounts WHERE CellphoneID='{CellphoneID}'")
result = cursor.fetchone()

if result is not None:
    balance = result[0]
else:
    print("You're not authrorized to make calls")
    exit()


caller_balance = balance
print(caller_balance)

call_duration = str(caller_balance * 60) 

def get_event(events):
    print(events.get('Event'))

def callback_events(events):
    print(events)
        
def on_action_successful(response):
    print("Action Completed successfully")
    
def handle_bridge_enter(event):
    print(f"Channel {event.get_header('Channel')} entered bridge {event.get_header('BridgeUniqueid')}")


ami.add_event_listener('BridgeEnter')



ami.logoff()

mydb.close()