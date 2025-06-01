import random
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~'
]
x = input("Please enter your full name")
name = x.split(" ")
if len(name) == 2:
    fn = name[0]
    ln = name[1]
    username1 = fn[2:5]+str(random.randint(1,10))+random.choice(special_characters)+ln[1:3]+str(random.randint(1,10))+random.choice(special_characters)
    username2 = fn[:3]+str(random.randint(1,5))+ln[3:4]+str(random.randint(1,10))+random.choice(special_characters)
    print(f"Here are two options: \n1: {username1}\n2: {username2}")
if len(name) == 3:
    fn = name[0]
    mn = name[1]
    ln = name[2]
    username1 = fn[2:5]+str(random.randint(1,10))+random.choice(special_characters)+mn[:3]+random.choice(special_characters)+ln[1:3]+str(random.randint(1,10))+random.choice(special_characters)
    username2 = fn[:3]+str(random.randint(1,5))+mn[0:2]+str(random.randint(1,10))+ln[3:4]+str(random.randint(1,10))+random.choice(special_characters)
    print(f"Here are two options: \n1: {username1}\n2: {username2}")