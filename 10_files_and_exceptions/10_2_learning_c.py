from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()

for line in lines:
    new_line = line.replace('Python', 'C++')
    print(new_line)