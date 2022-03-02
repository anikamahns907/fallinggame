import turtle
import random

lives = 3
score = 0
#modules

wnd = turtle.Screen()
wnd.title("ufo attack")
wnd.bgcolor("black")
wnd.bgpic("sp.gif")
wnd.setup(width=800, height = 600)
wnd.tracer(0)


wnd.register_shape("player.gif")
wnd.register_shape("bad.gif")
wnd.register_shape("good.gif")


player = turtle.Turtle()
player.speed(0)
player.shape("player.gif")
player.color("black")
player.penup()
player.goto(0, -250)
player.direction = "right"

#create pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 250)
font = ("courier", 24, "normal" )
pen.write("score: " + str(score) + " lives: " + str(lives), align = "center", font = font)


# good sprite list 
good_sprites = []

for _ in range(3):
    good = turtle.Turtle()
    good.speed(0)
    good.shape("good.gif")
    good.color("blue")
    good.penup()
    good.goto(random.randint(-380,380), random.randint(-380,380))
    good.speed = random.randint(1,4)
    good_sprites.append(good)


# good sprite list 
bad_sprites = []

for _ in range(3):
    bad = turtle.Turtle()
    bad.speed(0)
    bad.shape("bad.gif")
    bad.color("red")
    bad.penup()
    good.goto(random.randint(-380,380), random.randint(-380,380))
    bad.speed = random.randint(1,4)
    bad_sprites.append(bad)







#functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"


# jeboard binding
wnd.listen()
wnd.onkeypress(go_left, "Left")
wnd.onkeypress(go_right, "Right")

while True:
    wnd.update()

    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    #move the good guy
    y = good.ycor()
    y -= good.speed
    good.sety(y)

    #move the good guy
    y = bad.ycor()
    y -= bad.speed
    bad.sety(y)

    for good in good_sprites:
        y = good.ycor()
        y-= 3
        good.sety(y)

        #check if off screen
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(-380,380)
            good.goto(x,y)

        #check for collision with player
        if good.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(-380,380)
            good.goto(x,y)
            score+=10
            pen.clear()
            pen.write("score: " + str(score) + " lives: " + str(lives), align = str("center"), font = font)

    for bad in bad_sprites:
        y = bad.ycor()
        y-= 3
        bad.sety(y)


        #check if off screen
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(-380,380)
            bad.goto(x,y)

        #check for collision with player
        if bad.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(-380,380)
            bad.goto(x,y)
            score-=10
            lives -=1
            pen.clear()
            pen.write("score:" + str(score) + "lives" + str(lives), align =  str("center"), font = font)

            




wnd.mainloop()
