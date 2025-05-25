names = []
while True:
    print ("1. Add Name \n2. Remove Name \n3. Display List \n4. Quit")
    choice = int(input("Please select an option"))
    if choice == 1:
        add = input("What name would you like to add?")
        names.append(add)
    elif choice == 2:
        remove = input("What name would you like to remove?")
        names.remove(remove)
    elif choice == 3:
        print(names)
    elif choice == 4:
        break
    else:
        print ("Invalid Choice")
        continue