import mysql.connector
from pyami_asterisk import AMIClient

mydb = mysql.connector.connect(
    host = "54.36.181.102", 
    user = "Jaheim",
    password = "password",
    database = "asterisk_call"
)

Username = "Docker"
cursor = mydb.cursor()
cursor.execute(f"SELECT Balance FROM Dialplan WHERE Name='{Username}'")
result = cursor.fetchone()

if result is not None:
    balance = result[0]
else:
    print("You're not authrorized to make calls")
    exit()
    
caller_balance = balance
print(type(caller_balance))

amount = int(caller_balance)
print(type(amount))

call_duration = str(amount * 60)
print(call_duration)
print(type(call_duration))

def all_events(events):
    if events.get('Event') == "BridgeEnter":
        ami.create_action({
            "Action":"AbsoluteTimeout",
            "Channel": events.get('Channel'),
            "Timeout" : call_duration
        },callback_originate
    )

def callback_originate(events):
    print(events)
    
def get_event(events):
    if events.get('Event') == "BridgeEnter":
        ami.create_action({
            "Action":"AbsoluteTimout",
            "Channel" : 'Channel',
            "Timeout" : "5"
        },callback_originate
    )

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

ami.connect()

"""
    The database was called Asterisk and the table was called Callers
    the contents of the table are PersonID, Balance and Name
"""
