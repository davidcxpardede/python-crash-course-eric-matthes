from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text().rstrip()

for line in contents.splitlines():
    new_line = line.replace('Python', 'JavaScript')
    print(new_line)