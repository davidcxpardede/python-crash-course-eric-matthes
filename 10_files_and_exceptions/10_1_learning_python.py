from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

print("\n\n")
lines = contents.splitlines()
for line in lines:
    print(line)