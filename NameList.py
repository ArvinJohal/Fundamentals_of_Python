names = []
while True:
    print ("1. Add Name \n2. Remove Name \n3. Display List \n4. sort ascending \n5. sort descending \n6. Slice \n7. Quit")
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
        names.sort()
        print(names)
    elif choice == 5:
        names.sort(reverse=True)
        print(names)
    elif choice == 6:
        starting_value = int(input("Please choose a starting value"))
        slicing = int(input("Please choose a number to slice from"))
        print (names[starting_value-1:slicing])
    elif choice == 7:
        break
    else:
        print ("Invalid Choice")
        continue
