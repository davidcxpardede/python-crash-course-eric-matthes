'''
Modify the make_shirt(function) so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''

def make_shirt(size='L', text='I love Python'):
    """Create a shirt based on the size and text-to-print provided by user.
    """
    print(f"Your t-shirt's size is {size.upper()} with the text '{text}'.")

make_shirt()
make_shirt('m')
make_shirt('s', 'I love David!')