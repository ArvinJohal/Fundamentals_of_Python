import random
row = []
column = []
for i in range (5):
    row.append('-')
for i in range (5):
    column.append(row)
def print_grid():
    for row in column:
        print(''.join(row))
print ("Welcome to the treasure hunt. You will have 5 guesses and recieve clues as to where the treasure is on a 5x5 map")
print_grid()

def place_treasure():
    tr,tc = random.randint(0,4),random.randint(0,4)
    print ("The treasure has been placed!")
    return tr,tc
tr,tc = place_treasure()
r = int(input("Please enter the number of the row you would like to select: "))
c = int(input("Please enter the number of the column you would like to select: "))