import os
import json
from pathlib import Path


def clear():
    input("Press Enter to Continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR = Path(__file__).resolve().parent

def updateDatabase(users = []):
    with open(f"{BASE_DIR}/auth/users.json", 'r+', encoding='utf-8') as file:
        file.seek(0)
        json.dump(users, file, ensure_ascii=False, indent=4)
        file.truncate()

def createRandomPassword():
    pass

def randomizePassword():
    pass
