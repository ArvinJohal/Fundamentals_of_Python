import random
# row = []
# column = []
# for i in range (5):
#     row.append('-')
# for i in range (5):
#     column.append(row)
column = [['-' for i in range (5)]for j in range (5)]
def print_grid():
    global column
    for row in column:
        print(''.join(row))
def place_treasure():
    tr,tc = random.randint(0,4),random.randint(0,4)
    print ("The treasure has been placed!")
    return tr,tc
tr,tc = place_treasure()
print ("Welcome to the treasure hunt. You will have 5 guesses and recieve clues as to where the treasure is on a 5x5 map")
guesses = 5
while True:
    print_grid()


    r = int(input("Please enter the number of the row you would like to select (0-4): "))
    c = int(input("Please enter the number of the column you would like to select (0-4): "))
    column[r][c] = "x"
    guesses = guesses - 1
    if r > tr:
        print ("You are too far down")
        print (f"You have {guesses}: guesses remaining")
    elif r < tr:
        print ("You are too far up")
        print (f"You have {guesses}: guesses remaining")
    elif r == tr:
        print ("The row is correct!")
        if c > tc:
            print ("You are too far right")
            print (f"You have {guesses}: guesses remaining")
        elif c < tc:
            print ("You are too far left")
            print (f"You have {guesses}: guesses remaining")
    if r == tr and c == tc:
        print (f"Congratulations!!! You found the treasure with: {guesses} guesses remaining! ")
        break
    if guesses == 0:
        print ("You have run out of guesses :(")
        break
