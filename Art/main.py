import turtle
import random
import time
# Function to generate random RGB color tuples
def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate list of 100 random RGB color tuples
random_colors = [generate_random_color() for _ in range(100)]


#setting turtle
pointer = turtle.Turtle()

turtle.colormode(255)

#screen settings
scr = turtle.Screen()
scr.setup(width=500, height=500)

pointer.up()
pointer.goto(-125,-125)
pointer.speed("slow")
pointer.down()


for position in range(4):
    pointer.forward(225)
    pointer.left(90)


pointer.clear()


pointer.up()
pointer.speed("fastest")
pointer.goto(0,0)
pointer.down()
for position in range(100):
    pointer.circle(100)
    pointer.setheading(pointer.heading() + 10)


pointer.clear()



pointer.goto(-210,-210)
pointer.speed("slow")
a = pointer.heading()
print(a)
pointer.left(360-a)
for position in range(10):
    y = 20
    pointer.dot(y, random.choice(random_colors))
    pointer.forward(420)
    y +=20
    pointer.goto(-420, -210 + y)
    




scr.exitonclick()
