import turtle
import random
import time
win = turtle.Screen()
win.register_shape("spaceship.gif")
win.register_shape("Asteroid1.gif")
win.register_shape("Asteroid_2.gif")
win.register_shape("Bomb.gif")
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
Asteroids= ["Asteroid1.gif","Asteroid_2.gif"]
Enemies = []
def spawn_enemy():
    enemy = turtle.Turtle()
    enemy.hideturtle()
    enemy.up()
    shape = random.choice(Asteroids)
    enemy.shape(shape)
    if random.random() < 0.1:
        shape = "Bomb.gif"
        enemy.shape(shape)
        enemy.is_bomb = True
    else:
        enemy.is_bomb = False
    x = random.randint(-300,300)
    y = random.randint(200,300)
    enemy.hideturtle()
    enemy.goto(x,y)
    enemy.showturtle()
    Enemies.append(enemy)
spawn_interval = 2
last_spawn_time = time.time()
run = True
while run == True:
    win.update()
    current_time = time.time()
    if current_time - last_spawn_time > spawn_interval:
        spawn_enemy()
        last_spawn_time = current_time
    #move the enemies
    for enemy in Enemies[:]:
        enemy.sety(enemy.ycor()-random.randint(10,15))
        if enemy.ycor()<-300:
            Enemies.remove(enemy)
            enemy.hideturtle()
win.mainloop()