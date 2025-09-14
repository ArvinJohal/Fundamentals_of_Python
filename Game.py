import turtle
win = turtle.Screen()
win.register_shape("spaceship.gif")
win.register_shape("Asteroid1.gif")
dart = turtle.Turtle()
dart.shape("spaceship.gif")
dart.hideturtle()
dart.setheading(90)
dart.up()
dart.sety(-200)
dart.showturtle()
def left():
    x = dart.xcor()
    if x>-300:
        dart.setx(x-50)
win.listen()
win.onkey(left,"Left")
def right():
    x = dart.xcor()
    if x<300:
        dart.setx(x+50)
win.onkey(right,"Right")
def spawn_enemy():
    Asteroids= ["Asteroid1.gif"]

turtle.done()