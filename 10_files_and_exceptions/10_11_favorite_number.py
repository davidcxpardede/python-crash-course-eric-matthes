from pathlib import Path
import json

path = Path('10_files_and_exceptions/favorite_number.json')

favorite_number = input("What is your favorite number? ")
contents = json.dumps(favorite_number)
path.write_text(contents)