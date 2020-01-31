# Write your code here :-)
import pygame
import turtle
#import winsound
import pygame

import os
pygame.font.init()

large = pygame.font.Font("FreightSansBold.otf", 85)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)
#### FOR MAIN ####
HEADING = large.render("PADDLE", True, (255,255,255))

PLAY= medium.render("PLAY", True, (255,255,0))
PLAY_H = medium.render("PLAY", True, (200,0,200))

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('BALL')

BACKGROUND = pygame.image.load(os.path.join("images","earth.jpg")).convert()

play= (250, 140, 230, 40)



def showMain():
    WHITE = (255,255,255)

    win.blit(BACKGROUND, (0, 0))
    win.blit(HEADING,(85,20))




    win.blit(PLAY, (play[0],play[1]))


running = True
while running:
    pygame.display.flip()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            #singleplayer
            if play[0] < x < (play[0]+play[2]) and play[1] < y < (play[1]+play[3]):






                wn = turtle.Screen()
                wn.title("THE SPARKLING STARS")
                wn.bgcolor("black")
                wn.setup(width=800, height=600)
                wn.tracer(0)





                # Score
                score_a = 0
                score_b = 0

                # Paddle A
                paddle_a = turtle.Turtle()
                paddle_a.speed(0)
                paddle_a.shape("square")
                paddle_a.color("green")
                paddle_a.shapesize(stretch_wid=5,stretch_len=1)
                paddle_a.penup()
                paddle_a.goto(-350, 0)

                # Paddle B
                paddle_b = turtle.Turtle()
                paddle_b.speed(0)
                paddle_b.shape("square")
                paddle_b.color("red")
                paddle_b.shapesize(stretch_wid=5,stretch_len=1)
                paddle_b.penup()
                paddle_b.goto(350, 0)

                # Ball
                ball = turtle.Turtle()
                ball.speed(8)
                ball.shape("circle")
                ball.color("white")
                ball.penup()
                ball.goto(0, 0)
                ball.dx = 0.1
                ball.dy = 0.1

                # Pen
                pen = turtle.Turtle()
                pen.speed(0)
                pen.color("white")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 260)
                pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


                # Functions
                def paddle_a_up():
                    y = paddle_a.ycor()
                    y += 20
                    paddle_a.sety(y)

                def paddle_a_down():
                    y = paddle_a.ycor()
                    y -= 20
                    paddle_a.sety(y)

                def paddle_b_up():
                    y = paddle_b.ycor()
                    y += 20
                    paddle_b.sety(y)

                def paddle_b_down():
                    y = paddle_b.ycor()
                    y -= 20
                    paddle_b.sety(y)

                # Keyboard bindings
                wn.listen()
                wn.onkeypress(paddle_a_up, "w")
                wn.onkeypress(paddle_a_down, "s")
                wn.onkeypress(paddle_b_up, "Up")
                wn.onkeypress(paddle_b_down, "Down")

                # Main game loop
                while True:
                    wn.update()

                    # Move the ball
                    ball.setx(ball.xcor() + ball.dx)
                    ball.sety(ball.ycor() + ball.dy)



                    # Top and bottom
                    if ball.ycor() > 290:
                        ball.sety(290)
                        ball.dy *= -1
                        winsound.PlaySound ("bounce.wav", winsound.SND_ASYNC)

                    elif ball.ycor() < -290:
                        ball.sety(-290)
                        ball.dy *= -1
                        winsound.PlaySound ("bounce.wav", winsound.SND_ASYNC)

                    #Left and right
                    if ball.xcor() > 350:
                        score_a += 1
                        pen.clear()
                        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                        ball.goto(0, 0)
                        ball.dx *= -1

                    elif ball.xcor() < -350:
                        score_b += 1
                        pen.clear()
                        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                        ball.goto(0, 0)
                        ball.dx *= -1


                    # Paddle and ball collisions
                    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() - 50:
                        ball.dx *= -1
                        winsound.PlaySound ("bounce.wav", winsound.SND_ASYNC)

                    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
                        ball.dx *= -1
                        winsound.PlaySound ("bounce.wav", winsound.SND_ASYNC)



        showMain()
        x,y = pygame.mouse.get_pos()
        if play[0] < x < (play[0]+play[2]) and play[1] < y < (play[1]+play[3]):

           win.blit(PLAY_H, (play[0], play[1]))







pygame.quit()
