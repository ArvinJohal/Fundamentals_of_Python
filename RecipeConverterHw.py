def tbsp_tsp(amount):
    tsp = round(amount*3,2)
    print(f"The amount of teaspoons required are: {tsp} teaspoons")
def tsp_tbsp(amount):
    tbsp = round(amount/3,2)
    print(f"The amount of tablespoons required are: {tbsp} tablespoons")
def tsp_cup(amount):
    cup = round(amount*0.0208,2)
    print(f"The amount of cups required are: {cup} cups")
def cup_tsp(amount):
    tsp = round(amount*48,2)
    print(f"The amount of tsps required are: {tsp} tsps")
def tbsp_cup(amount):
    cup = round(amount*0.0625,2)
    print(f"The amount of cups required are: {cup} cups")
def cup_tbsp(amount):
    tbsp = round(amount*16,2)
    print(f"The amount of tbsps required are: {tbsp} tbsps")

while True:
    print ("1. tbsp to tsp \n2. tsp to tbsp \n3. tsp to cup \n4. cup to tsp \n5. tbsp to cup \n6. cup to tbsp \n7. Quit")
    choice = int(input("Please select a number for the converion you would like"))
    if choice == 1:
        amount = float(input("Please enter the amount of tbsps"))
        tbsp_tsp(amount)
    elif choice == 2:
        amount = float(input("Please enter the amount of tsps"))
        tsp_tbsp(amount)
    elif choice == 3:
        amount = float(input("Please enter the amount of tsps"))
        tsp_cup(amount)
    elif choice == 4:
        amount = float(input("Please enter the amount of cup"))
        cup_tsp(amount)
    elif choice == 5:
        amount = float(input("Please enter the amount of tbsps"))
        tbsp_cup(amount)
    elif choice == 6:
        amount = float(input("Please enter the amount of cups"))
        cup_tbsp(amount)
    elif choice == 7: 
        break
