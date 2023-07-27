from pathlib import Path

guest_book = ''

while True:
    guest = input("Please write your name. Enter 'q' to quit. ")
    
    if guest.lower() == 'q':
        break
    
    guest_book += guest
    guest_book += "\n"

path = Path('10_files_and_exceptions/guest_book.txt')
path.write_text(guest_book)
print(guest_book)
    