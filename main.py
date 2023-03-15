from asterisk.ami import AMIClient , SimpleAction

client = AMIClient(address="54.36.181.102", port=5038)
client.login(username='manager' , secret="123456")

Trail = SimpleAction(
    'Originate',
    Channel = 'SIP/Test2/4321',
    Exten='1234',
    Priority=1,
    Context='Test',
)

response = client.send_action(Trail)

print(response)

client.logoff()

'''while True:
    event = client.receive_event()
    if event.name == "Newstate" and event.chanel =='SIP/Tester1' and event.state == "Up":
        break'''
    
# response = client.hangup(channel='SIP/Tester1')

'''Action:Login
Username:manager
Secret:123456'''