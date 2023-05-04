from pyami_asterisk import AMIClient

def callback_originate(events):
    print(events)

ami = AMIClient(host='54.36.181.102', port=5038, username='manager' , secret='im')

ami.create_action(
    {
        "Action": "Originate",
        "Channel": "SIP/Admin",
        "Timeout": "20000",
        "Exten": "4000",
        "Context": "Trial",
        "Async": "true",
        "Priority": "1",
        "CallerID": "Python"
    },
    callback_originate,
)
ami.connect()