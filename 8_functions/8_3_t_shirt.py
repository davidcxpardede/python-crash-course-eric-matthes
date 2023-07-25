'''
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''

def make_shirt(size, text):
    """Create a shirt based on the size and text-to-print provided by user.
    """
    print(f"Your t-shirt's size is {size.upper()} with the text '{text}'.")

make_shirt('M', 'I love Physics')
make_shirt(text='Your mom is hot', size='l')