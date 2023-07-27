from pathlib import Path

name = input("What is your name? ")
path = Path('10_files_and_exceptions/name.txt')
path.write_text(name)