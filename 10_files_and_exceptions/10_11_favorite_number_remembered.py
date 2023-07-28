from pathlib import Path
import json

path = Path('10_files_and_exceptions/favorite_number.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"Your favorite number is {favorite_number}.")
else:
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"Your favorite number, {favorite_number}, has been saved!")



