from utils import BASE_DIR, clear, updateDatabase
import datetime
import json

def login(username, password):
    users = []
    with open(f'{BASE_DIR}/auth/users.json', 'r', encoding="utf-8") as file:
        users = json.load(file)

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                user['last-activity'] = str(datetime.datetime.now())
                updateDatabase(users)
                print("You are now Logged in enjoy")
                clear()
                return True
            else:
                print("Invalid Password!")
                clear()
                return False
        else:
            print("User Does not Exists! Please Register One Before logging in")
            return False

def register(username, password):
    user = {'username': username, 'password': password}
    with open(f'{BASE_DIR}/auth/users.json', 'r+', encoding='utf-8') as file:
        users = json.load(file)
        users.append(user)
        file.seek(0)
        json.dump(users, file, ensure_ascii=False, indent=4)
        file.truncate()
    print("You can now Log In!")
    clear()
    return True

def isLoggedIn(authStatus):
    return authStatus