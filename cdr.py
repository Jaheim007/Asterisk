import mysql.connector
from pyami_asterisk import AMIClient

mydb = mysql.connector.connect(
    host = "54.36.181.102",
    user = "Jaheim",
    password = "password",
    database = "asterisk_call"
)

Db_name = "Docker"
cursor = mydb.cursor()
cursor.execute(f"SELECT Balance FROM Dialplan Where Name='{Db_name}'")
result = cursor.fetchone()

if result is not None:
    balance = result[0]
    
else:
    print("You don't have a value in the db.")
    
caller_balance = balance
print(caller_balance)

value_per_minute = 50 * 60

value_duration = value_per_minute
print(value_duration)

call_limit = str(caller_balance / 50)
print(call_limit)

def all_events(events):
    if events.get('Event') == "BridgeEnter":
        ami.create_action({
            "Action":"AbsoluteTimeout",
            "Channel": events.get('Channel'),
            "Timeout" : call_limit
        }, callback_originate
    )
        
def callback_originate(events):
    print(events)
    
def get_event(events):
    if events.get("Event") == "Cdr":
        print(events)
    
ami = AMIClient(host='54.36.181.102', port=5038, username='Nan' , secret='nan')

ami.create_action(
    {
        "Action": "Originate",
        "Channel": "PJSIP/7001",
        "Timeout": "20000",
        "Exten": "200",
        "Context": "Action",
        "Async": "true",
        "Priority": "1",
    },
    all_events,
)

ami.register_event(["*"], all_events)
ami.register_event(["*"], get_event)

mydb.close()

ami.connect()
