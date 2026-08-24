# Problem 10-12: Favorite Number Remembered

from pathlib import Path
import json

def get_favorite_no(path):
    if path.exists():
        content = path.read_text()
        fav_no = json.loads(content)
        return fav_no
    else:
        return None

def save_favorite_no(path):
    while True:
        try:
            fav_no = int(input("Please enter your favourite number (0,1,2,....): "))
            break
        except:
            print("\nEnter a number in numerical format!\n")
    content = json.dumps(fav_no)
    path.write_text(content)
    print("I'll remember your favourite no!")
    return fav_no

def favorite_number():
    path = Path('favorite_no.json')
    fav_no = get_favorite_no(path)
    if fav_no:
        print(f"I remember your favourite no. It's {fav_no}!")
    else:
        fav_no = save_favorite_no(path)

favorite_number()