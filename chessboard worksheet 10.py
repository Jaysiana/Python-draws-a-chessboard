''' Week 10, homework problem 1
Write a program that prompts the user for two integers, m and n,
and draws a grid of m by n cells with the turtle.
'''

from turtle import *

# A function to draw parallel lines.
# Parameters:
# * nlines - number of lines
# * length - length of each line
# * dist - distance between adjacent lines
def drawlines(nlines, length, dist):
    for i in range(nlines):
        pendown()
        forward(length)
        penup()
        left(180)
        forward(length)
        if i < nlines - 1:
            left(90)
            forward(dist)
            left(90)

# Get user input
m = int(input("Enter m: "))
n = int(input("Enter n: "))

d = 45  # Side length of the square

# Set up the canvas
setup(800, 600)
speed(3)
penup()
left(90)
forward(int(m / 2 * d))
left(90)
forward(int(n / 2) * d)
left(180)

# Draw horizontal lines
drawlines(m + 1, n * d, d)

right(90)

# Draw vertical lines
drawlines(n + 1, m * d, d)
stepscount=0
def fill():
    begin_fill()
    for i in range(4):
        forward(d)
        right(90)
    forward(d)
    end_fill()
def moveback():
    penup()
    backward(n*d)
    right(90)
    forward(d)
    left(90)
#1st row
x=0
verticalsteps=0
rowcount=0

right(90)
stepscount=0
while verticalsteps!=m:
        
    while stepscount != n:
        fill()
        stepscount+=1
        if stepscount!=n:
            forward(d)
            stepscount+=1
        else:
            break
    moveback()
    stepscount=0
    verticalsteps+=1
    rowcount+=1
    if rowcount%2!=0:
        forward(d)
        stepscount+=1
        pendown()
    else:
        pendown()
#2nd row


# Finish
#hideturtle()
exitonclick()