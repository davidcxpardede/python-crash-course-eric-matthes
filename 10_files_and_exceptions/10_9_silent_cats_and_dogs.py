from pathlib import Path

try:
    
    path_cats = Path('10_files_and_exceptions/cats.txt')
    path_dogs = Path('10_files_and_exceptions/dogs.txt')

    cats = path_cats.read_text(encoding='utf-8').rstrip()
    dogs = path_dogs.read_text(encoding='utf-8').rstrip()
    
    print("\nThe name of the cats are: ")
    
    for cat in cats.splitlines():
        print(cat)
    
    print("\nThe name of the dogs are: ")
    for dog in dogs.splitlines():
        print(dog)
        
except FileNotFoundError:
    pass