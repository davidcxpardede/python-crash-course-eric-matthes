'''
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
'''

def send_messages(messages, sent_messages):
    """Print the messages and move them to a new list."""
    for message in messages:
        print(message)
    
    while messages:
        sent_messages.append(messages.pop())

list_of_messages = ['Hello!', 'Can you call me back?', 'Where are you?', 'Are you busy?', 'Please text me back.', 'WAKANDA FOREVER!']

list_of_sent_messages = []

send_messages(list_of_messages[:], list_of_sent_messages)

print(list_of_messages)
print(list_of_sent_messages)