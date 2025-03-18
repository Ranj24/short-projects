import random
import string
from threading import Timer
from turtle import Turtle, Screen

from numba.core.ir import Print

colour_list = ['red', 'blue', 'yellow', 'cyan', 'magenta', 'black']

def set_speed(turtle: Turtle):
    turtle.speed(random.randint(0,10))


def create_turtle(colours: list, width : int, height : int):
    start_pos = (height-10)/len(colour_list)
    y_pos = (height/2)-50
    turtle_list = []
    x_pos = (width/2) - 50
    turtle = Turtle()
    for color in colour_list:
        turtle.color(color)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.shape('turtle')
        new_turtle.shapesize(1, 1, 3)
        new_turtle.goto(-x_pos, y_pos)
        new_turtle.showturtle()
        turtle_list.append(new_turtle)
        y_pos -= start_pos
    return turtle_list

def end_race(turtle_list: list[Turtle], guess: string):
    for turtle in turtle_list:
        if (turtle.xcor()) >= 450:
            turtle.setheading(0)
            turtle.shapesize(2, 2, 5)
            turtle.home()
            if guess == turtle.color():
                print("You win!")
            else:
                print("You lose!")
            return True
    return False

if __name__ == "__main__":
    width = 1000
    height = 600
    screen = Screen()
    screen.setup(width,height)
    screen.bgcolor("DarkGreen")
    guess = screen.textinput("Let's race", "Pick your turtle ['red', 'blue', 'yellow', 'cyan', 'magenta', 'black']:")
    turtle_list = create_turtle(colour_list,width,height)
    print(end_race(turtle_list, guess))
    while not end_race(turtle_list, guess):
        for turtle in turtle_list:
            set_speed(turtle)
            turtle.forward(random.randint(40,45))


    screen.exitonclick()