import random
import time
import os
letters = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e',
    'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
    'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y',
    'Z', 'z']
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~'
]
while True:
    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)
    d = str(random.randint(0,9))
    e = str(random.randint(0,9))
    f = str(random.randint(0,9))
    g = random.choice(special_characters)
    h = random.choice(special_characters)

    variables = [a,b,c,d,e,f,g,h]
    random.shuffle(variables)
    password = ""
    for ch in variables:
        password += ch
    print (f"This is your password, this message will delete in 5 secs: {password}")
    time.sleep(5)
    os.system("cls")
    choice = input("Would you like a different password (Y or N) ")
    if choice == "Y":
        continue
    elif choice == "N":
        break 
    else:
        print ("Invalid Input")
        choice = input("Would you like a different password (Y or N)")
