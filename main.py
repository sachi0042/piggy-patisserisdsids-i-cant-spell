import turtle
import random
import winsound

score=0
lives=10

#making window
wn = turtle.Screen()
wn.title("Feed the pig??")
wn.bgcolor("pink")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#registering images
wn.register_shape("piggy.gif")
wn.register_shape("cake.gif")
wn.register_shape("roll.gif")
wn.register_shape("cake_ice.gif")
wn.register_shape("pancakes.gif")
wn.register_shape("mixer.gif")
wn.register_shape("oven.gif")
wn.register_shape("whisk.gif")


#song
winsound.PlaySound("Genshin_lofi.wav" ,flags =winsound.SND_ASYNC)

#adding player
pig = turtle.Turtle()
pig.speed(0)
pig.shape("piggy.gif")
pig.color("white")
pig.penup()
pig.goto(0, -240)
pig.direction = "stop"

#list of good things
cakes =[] #red, speed= 1, score= 10
rolls =[] #orange, speed= 1, score 10
cake_ices =[] #yellow, speed= 1.5, score 20
pancakes =[] #green, speed= 1.5, score 20

#list of bad things
mixers =[] #purple
ovens =[] #pink
whisks =[] #black

#adding cake/good
for _ in range(2):
    cake = turtle.Turtle()
    cake.speed(0)
    cake.shape("cake.gif")
    cake.color("red")
    cake.penup()
    cake.goto(0, 250)
    cake.direction = "stop"
    cakes.append(cake)

#adding rolls/good
for _ in range(2):
    roll= turtle.Turtle()
    roll.speed(0)
    roll.shape("roll.gif")
    roll.color("orange")
    roll.penup()
    roll.goto(0, 250)
    roll.direction = "stop"
    rolls.append(roll)

#adding cake_ice/good
for _ in range(1):
    cake_ice = turtle.Turtle()
    cake_ice.speed(0)
    cake_ice.shape("cake_ice.gif")
    cake_ice.color("yellow")
    cake_ice.penup()
    cake_ice.goto(0, 250)
    cake_ice.direction = "stop"
    cake_ices.append(cake_ice)

#adding pancakes/good
for _ in range(1):
    pancake = turtle.Turtle()
    pancake.speed(0)
    pancake.shape("pancakes.gif")
    pancake.color("green")
    pancake.penup()
    pancake.goto(0, 250)
    pancake.direction = "stop"
    pancakes.append(pancake)


#adding mixers/bad
for _ in range(1):
    mixer= turtle.Turtle()
    mixer.speed(0)
    mixer.shape("mixer.gif")
    mixer.color("purple")
    mixer.penup()
    mixer.goto(0, 250)
    mixer.direction = "stop"
    mixers.append(mixer)

#adding ovens/bad
for _ in range(1):
    oven= turtle.Turtle()
    oven.speed(0)
    oven.shape("oven.gif")
    oven.color("pink")
    oven.penup()
    oven.goto(0, 250)
    oven.direction = "stop"
    ovens.append(oven)

#adding whisks/bad
for _ in range(1):
    whisk= turtle.Turtle()
    whisk.speed(0)
    whisk.shape("whisk.gif")
    whisk.color("black")
    whisk.penup()
    whisk.goto(0, 250)
    whisk.direction = "stop"
    whisks.append(whisk)

#displaying score and lives
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.goto(0, 250)
font = ("Times", 30, "bold")
pen.write("Score: {} Lives: {}".format(score, lives),align="center", font=font)

# Functions
def go_left():
    pig.direction = "left"

def go_right():
    pig.direction = "right"

# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main game loop
while True:
    #updateing screen
    wn.update()
    #making pig move left
    if pig.direction =="left":
        x=pig.xcor()
        x-=1
        pig.setx(x)

    #making pig move right
    if pig.direction == "right":
        x = pig.xcor()
        x+=1
        pig.setx(x)

    #barrier thing/right
    if pig.xcor() > 350:
        pig.setx(350)
        x -=1
        pig.setx(x)

    # barrier thing/left
    if pig.xcor() < -350:
        pig.setx(-350)
        x += 1
        pig.setx(x)


    #cakes movement
    for cake in cakes:
        y =cake.ycor()
        y-=1
        cake.sety(y)

        #repeating
        if y < -300:
            x=random.randint(-350, 350)
            y = random.randint(350, 350)
            cake.goto(x,y)

        #check for collision
        if cake.distance(pig)<40:
            x = random.randint(-350, 350)
            y = random.randint(350, 350)
            cake.goto(x, y)
            score += 10
            lives -= 0
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    #rolls movement
    for roll in rolls:
        y = roll.ycor()
        y -=0.5
        roll.sety(y)

        #repeating
        if y < -300:
            x = random.randint(-350, 350)
            y = random.randint(350, 350)
            roll.goto(x, y)

        # check for collision
        if roll.distance(pig) < 40:
            x = random.randint(-350, 350)
            y = random.randint(350, 350)
            roll.goto(x, y)
            score += 15
            lives -= 0
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    #cake_ice movement
        for cake_ice in cake_ices:
            y = cake_ice.ycor()
            y -=0.45
            cake_ice.sety(y)

            #repeating
            if y < -300:
                x = random.randint(-350, 350)
                y = random.randint(350, 350)
                cake_ice.goto(x, y)

            # check for collision
            if cake_ice.distance(pig) < 40:
                x = random.randint(-350, 350)
                y = random.randint(350, 350)
                cake_ice.goto(x, y)
                score += 15
                lives -= 0
                pen.clear()
                pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    #pancakes movement
        for pancake in pancakes:
            y = pancake.ycor()
            y -=0.8
            pancake.sety(y)

            #repeating
            if y < -300:
                x = random.randint(-350, 350)
                y = random.randint(350, 350)
                pancake.goto(x, y)

            # check for collision
            if pancake.distance(pig) < 40:
                x = random.randint(-350, 350)
                y = random.randint(350, 350)
                pancake.goto(x, y)
                score += 15
                lives -= 0
                pen.clear()
                pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    #mixers movement
            for mixer in mixers:
                y = mixer.ycor()
                y -=1
                mixer.sety(y)

                #repeating
                if y < -300:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    mixer.goto(x, y)

                # check for collision
                if mixer.distance(pig) < 40:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    mixer.goto(x, y)
                    score += 0
                    lives -=1
                    pen.clear()
                    pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
    #ovens movement
            for oven in ovens:
                y = oven.ycor()
                y -=0.8
                oven.sety(y)

                #repeating
                if y < -300:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    oven.goto(x, y)

                # check for collision
                if oven.distance(pig) < 40:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    oven.goto(x, y)
                    score += 0
                    lives -=1
                    pen.clear()
                    pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
    #whisks movement
            for whisk in whisks:
                y = whisk.ycor()
                y -=0.5
                whisk.sety(y)

                #repeating
                if y < -300:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    whisk.goto(x, y)

                # check for collision
                if whisk.distance(pig) < 40:
                    x = random.randint(-350, 350)
                    y = random.randint(350, 350)
                    whisk.goto(x, y)
                    score += 0
                    lives -=1
                    pen.clear()
                    pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)



                    

wn.mainloop()