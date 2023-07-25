'''
Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. After calling the function, print both of your list to make sure the messages were moved correctly.
'''

def send_messages(messages, sent_messages):
    """Print the messages and move them to a new list."""
    for message in messages:
        print(message)
    
    while messages:
        sent_messages.append(messages.pop())

list_of_messages = ['Hello!', 'Can you call me back?', 'Where are you?', 'Are you busy?', 'Please text me back.', 'WAKANDA FOREVER!']

list_of_sent_messages = []

send_messages(list_of_messages, list_of_sent_messages)

print(list_of_messages)
print(list_of_sent_messages)