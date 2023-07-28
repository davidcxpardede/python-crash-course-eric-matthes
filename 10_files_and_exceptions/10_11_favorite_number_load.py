from pathlib import Path
import json

path = Path('10_files_and_exceptions/favorite_number.json')

contents = path.read_text()
favorite_number = json.loads(contents)
print(f"Your favorite number is {favorite_number}.")
