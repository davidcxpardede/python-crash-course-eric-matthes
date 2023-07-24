'''
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
- Think of five programming words you've learned about in the previous chapters. Use these wors as the keys in your glossary, and store their meanings as values.
- Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''

# rstrip()
# get()
# append()
# title()
# sorted()

python_syntaxes = {'strip()': 'Stripping whitespace from both end of a string.',
                   'get()': 'Accessing elements in a list or dictionaries.',
                   'append()':'Adding a new element to the end of a list.',
                   'title()':'Converting a string so that the first letter of each word is capitalized.',
                   'sorted()':'Sort a list permanently, in either ascending or descending order.',}

print(f"strip():\n\t{python_syntaxes['strip()']}")
print(f"get():\n\t{python_syntaxes['get()']}")
print(f"append():\n\t{python_syntaxes['append()']}")
print(f"title():\n\t{python_syntaxes['title()']}")
print(f"sorted():\n\t{python_syntaxes['sorted()']}")