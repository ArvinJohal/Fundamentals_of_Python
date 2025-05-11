import math
def square(side):
    area = side**2
    perimeter = side*4
    print ("Perimeter =", perimeter,"\n Area =", area)
def rectangle(width,length):
    area = length*width
    perimeter = length*2+width*2
    print ("Perimeter =", perimeter," Area =", area)
def triangle(base,p_height):
    area = (base*p_height)/2
    slanting_height = math.sqrt((base/2)**2 + p_height**2)
    perimeter = slanting_height*2 + base
    print ("Slanting height =",slanting_height, "Perimeter =", perimeter,"\n Area =", area)
def circle(radius):
    area = 3.14*radius**2
    circumference = 2*3.14*radius
    print ("circumference =", circumference,"\n Area =", area)
    
    
run = True
while run == True:
  print (" 1. Square \n 2. Rectangle \n 3. Triangle \n 4. Circle \n 5. Quit")
  x = int(input("Please select a number from the menu"))

  if x == 1:
    side = int(input("Enter the side length of your square:"))
    square(side)

    
  elif x == 2:
    length = int(input("Enter the length of your rectangle:"))
    width = int(input("Enter the width of your rectangle:"))
    rectangle(width,length)

  elif x == 3:
    base = int(input("Enter the base of your triangle:"))
    p_height = int(input("Enter the perpendicular height of your triangle:"))
    triangle(base,p_height)
    
  elif x == 4:
    radius = int(input("Enter the radius of your circle:"))
    circle(radius)

    
  elif x == 5:
    run = False
    print ("You have ended the program.")
  

