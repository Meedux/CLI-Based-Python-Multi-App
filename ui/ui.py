from auth.auth import login, register
from utils import clear
from getpass import getpass

def mainMenu(authStatus):
    if authStatus:
        print("Hello Welcome to the CLI Multi App!")
        print("1. Create a secure password")
        print("2. Use our CLI based Calculator")
        print("3. Play Our Games!!")
        print("4. SLUG")
        print("5. Exit")
        print("-------------------------------------")
    else:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("-------------------------------------")

def loginMenu():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    return login(username, password)    

def registerMenu():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    return register(username, password)

def gamesMenu():
    print("1. Random Guessing Number")
    print("2. Battleship")
    print("3. Hangman")
    print("4. Tic Tac Toe")
    print("5. Rock Paper Scissors")

def passwordMenu():
    print("1. Create a new random password")
    print("2. Randomize a password")


def hangManGame():
    pass

def battleShipGame():
    pass

def exitUI():
    pass

def ticTacToeGame():
    pass

def rockPaperScissors():
    pass

def slugGenerator():
    pass