import turtle
import random
import pygame
from pygame import mixer

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
wnd.register_shape("life.gif")
wnd.register_shape("playagain.gif")



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

lives_sprites = []
for i in range(3):
    life = turtle.Turtle()
    life.speed(0)
    life.shape("life.gif")
    if i ==0: 
        life.penup()
        life.setposition(350,260)
    if i ==1:
        life.penup()
        life.setposition(300,260)
    if i == 2:
        life.penup()
        life.setposition(250,260)

    lives_sprites.append(life)







def go_left():
    player.speed(0)
    player.backward(20)

def go_right():
    player.speed(0)
    player.forward(5)
        

def over_screen():
    wnd.clearscreen()
    wnd.bgcolor("black")
    pen.write("game over")

    
   

# jeboard binding
wnd.listen()
wnd.onkeypress(go_left, 'Left')
wnd.onkeypress(go_right, 'Right')


game_open = True
game_over = False
while game_open:
    while not game_over:
        wnd.update()

        

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

            if lives == 2:
                lives_sprites[2].hideturtle()
            if lives == 1:
                lives_sprites[2].hideturtle()
                lives_sprites[1].hideturtle()
            if lives <= 0:
                lives_sprites[2].hideturtle()
                lives_sprites[1].hideturtle()
                lives_sprites[0].hideturtle()
                game_over = True
    while game_over:
        over_screen()





            




          





wnd.mainloop()
