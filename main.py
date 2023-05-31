from asterisk.ami import AMIClient , SimpleAction

client = AMIClient(address="54.36.181.102", port=5038)
client.login(username='1024' , secret='1024')

def callback_events(events):
    print(events)

action = SimpleAction(
    'Originate',
    Channel = 'SIP/101',
    Exten='4000',
    Priority=1,
    Context='Tester',
)

response = client.send_action(action)

client.logoff()

'''while True:
    event = client.receive_event()
    if event.name == "Newstate" and event.chanel =='SIP/Tester1' and event.state == "Up":
        break'''
    
# response = client.hangup(channel='SIP/Tester1')

'''Action:Login
Username:manager
Secret:123456'''