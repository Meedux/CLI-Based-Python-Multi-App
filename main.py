from ui.ui import mainMenu, loginMenu, registerMenu, passwordMenu
from utils import clear
from password.password import createRandomPassword, randomizePassword
from calc.calc import calculate

def main():
    authStatus = False
    while True:
        mainMenu(authStatus)
        choice = input("Select an Input: ")

        if authStatus:
            match choice:
                case '1':
                    clear()
                    passwordMenu()
                    passChoice = input("Input your selection: ")
                    match passChoice:
                        case '1':
                            clear()
                            createRandomPassword()
                        case '2':
                            clear()
                            randomizePassword()
                        case _:
                            print("Invalid Input! Returning to main menu")
                            clear()

                case '2':
                    clear()
                    calculate()
                    clear()
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    print("Goodbye!")
                    clear()
                    break
                case _:
                    print("Invalid Input! Try again")
                    clear()
        else: 
            match choice:
                case '1':
                    authStatus = loginMenu()
                case '2':
                    registerMenu()
                case '3':
                    print("Goodbye!")
                    clear()
                    break
                case _:
                    print("Invalid Input! Try again")
                    clear()
            

if __name__ == "__main__":
    main()