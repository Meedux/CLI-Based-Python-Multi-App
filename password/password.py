from random import randrange, sample, choice, random
from utils import clear
import string

def createRandomPassword():
    text = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num = string.digits
    punctuation = string.punctuation

    numLower = int(input("How many lowercase text?: "))
    numUpper = int(input("How many uppercase text?: "))
    numNum = int(input("How many number(s)?: "))
    numPunctuation = int(input("How many punctuation(s): "))

    for i in range(0, numLower):
        text += lowercase[randrange(0, (len(lowercase) - 1))]

    for i in range(0, numUpper):
            text += uppercase[randrange(0, (len(uppercase) - 1))]

    for i in range(0, numNum):
            text += num[randrange(0, (len(num) - 1))]

    for i in range(0, numPunctuation):
            text += punctuation[randrange(0, (len(punctuation) - 1))]

    print(f"Here is your newly generated random password: {"".join(sample(text, len(text)))}")
    clear()

    

def randomizePassword():
    text = input("Type in your existing password here: ")
    extra = string.digits + string.punctuation 
    res = []

    for char in text:
        if char.isalpha():
            char = choice([char.upper(), char.lower()])
        res.append(char)

        if random() < 0.4:
            res.append(choice(extra))

    print(f"Here is your randomized password: {"".join(res)}")
    print(f"Here was your original password: {text}")
    clear()
