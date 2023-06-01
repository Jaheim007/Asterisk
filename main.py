from pyami_asterisk import AMIClient

def callback_originate(events):
    print(events)
    
def get_event(events):
    print(events.get('Event'))
    
def all_events(events):
    print(events)

ami = AMIClient(host='54.36.181.102', port=5038, username='1024' , secret='1024')

ami.create_action(
    {
        "Action": "Originate",
        "Channel": "SIP/101",
        "Timeout": "20000",
        "Exten": "7000",
        "Context": "Tester",
        "Async": "true",
        "Priority": "1",
    },
    callback_originate,
)
# ami.register_event(["*"], all_events)
ami.connect()

