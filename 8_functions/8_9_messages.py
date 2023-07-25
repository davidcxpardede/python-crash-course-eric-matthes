'''
Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
'''

def show_messages(messages):
    """Display the message in a list."""
    for message in messages:
        print(message)

list_of_messages = ['Hello!', 'Can you call me back?', 'Where are you?', 'Are you busy?', 'Please text me back.', 'WAKANDA FOREVER!']

show_messages(list_of_messages)