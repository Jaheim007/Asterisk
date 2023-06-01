from pyami_asterisk import AMIClient

def all_events(events):
    if events.get('Event') == "BridgeEnter":
        ami.create_action({
            "Action":"AbsoluteTimeout",
            "Channel": events.get('Channel'),
            "Timeout" : "5"
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

ami = AMIClient(host='54.36.181.102', port=5038, username='1024' , secret='1024')

ami.create_action(
    {
        "Action": "Originate",
        "Channel": "SIP/101",
        "Timeout": "20000",
        "Exten": "4000",
        "Context": "Tester",
        "Async": "true",
        "Priority": "1",
        "CallerID": "Python"
    },
    all_events,
)

ami.register_event(["*"], all_events)

ami.connect()




