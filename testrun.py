import time
import asterisk.manager
import datetime

ami = asterisk.manager.Manager()

ami.connect('54.36.181.102')

login_asterisk = ami.login('1024', '1024')

def get_event(events):
    print(events.get('Event'))

def callback_events(events):
    print(events)
    
current_timestamp = int(time.time())
print(current_timestamp)

absolute_timeout = current_timestamp + 30

dt = datetime.datetime.fromtimestamp(absolute_timeout)

print(absolute_timeout)

print(dt)

# try:
while True:
    action = {
        'Action': 'Originate',
        'Channel' : 'SIP/202',
        'Context' : 'Tester',
        'Exten' : '7000',
        'Priority' : '1', 
        'Timeout' : '30000',
        'AbsoluteTimeout': str(absolute_timeout)
    }
    
    callback_events(action)
    response = ami.send_action(action)
    get_event(response)
    print(response)

    # if response == "Success":
    #     if current_timestamp >= absolute_timeout:
    #         hangup_action = {
    #             'Action': 'Hangup',
    #             'Channel': 'SIP/101'  # Replace with the appropriate channel of the active call
    #         }
    #         response = ami.send_action(hangup_action)
            
# except TypeError:
#     print("Its gets out of the try")