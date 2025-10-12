list = [2,5,1,7,13,25,4]
found = False
counter = 0
search = int(input("What number would you like to search for?"))
for i in range(len(list)):
    if list[counter] == search:
        print (f"Number found at location {counter+1} ")
        found = True
        break
    else:
        counter = counter+1
        
if found == False:
    print(f"The number: {search} was not found")