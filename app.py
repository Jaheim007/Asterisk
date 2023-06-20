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

ami.connect()
