from pathlib import Path
import json

path = Path('10_files_and_exceptions/user.json')

name = input("What is your name? ")
nim = input("What is your student ID number? ")
major = input("What is your major? ")

user_info = {'name': name, 'nim': nim, 'major': major}
contents = json.dumps(user_info)
path.write_text(contents)

loaded_contents = path.read_text()
loaded_user_info = json.loads(loaded_contents)

print("\nUser Information:")
for info, value in loaded_user_info.items():
    print(f"{info.upper()}: {value.title()}")

