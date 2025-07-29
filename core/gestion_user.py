from dataclasses import dataclass, asdict
import json

@dataclass
class user_class:
    name : str
    age : int
    height : int
    weight : int

def create_user():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    height = input('Enter your height: ')
    weight = input('Enter your weight: ')
    user = user_class(name, age, height, weight)

    with open("../data/user.json","r") as outfile:
        old_json = json.load(outfile)

    old_json.append(asdict(user))

    with open("../data/user.json","w") as outfile:
        json.dump(old_json, outfile, indent=4)

def delete_user():
        with open("data/user.json","r") as outfile:
            old_json = json.load(outfile)

        removed = input('Enter your name: ')

        new_json = [user for user in old_json if user["name"] != removed]

        with open("data/user.json", "w") as f:
            json.dump(new_json, f, indent=4)

def edit_user():
    print("in work")


def main_part():
    choice = int(input('create 1, delete 2, edit 3 \nEnter your choice: '))
    if choice == 1:
        create_user()
    elif choice ==2:
        delete_user()
    elif choice ==3:
        edit_user()
    else:
        print("Bad choice")


if __name__ == "__main__":
    main_part()

