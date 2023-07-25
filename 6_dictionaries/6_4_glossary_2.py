'''
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print calls with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
'''

python_syntaxes = {'strip()': 'Stripping whitespace from both end of a string.',
                   'get()': 'Accessing elements in a list or dictionaries.',
                   'append()':'Adding a new element to the end of a list.',
                   'title()':'Converting a string so that the first letter of each word is capitalized.',
                   'sorted()':'Sort a list permanently, in either ascending or descending order.',
                   'items()':'A method to get all key-values pair in a dictionary.',
                   'keys()':'A method to get only the key names in a dictionary.',
                   'set()':'Getting only the unique entries in a dictionary or list.',
                   'pop()':'Removing an entry from a list',
                   'len()':'Finding the length of a list or string.',
                   'removeprefix()':'Removing a set of characters in the beginning of a string (prefixes).',}

for syntaxes, description in sorted(python_syntaxes.items()):
    print(f"Syntax: {syntaxes}\n{description}\n")