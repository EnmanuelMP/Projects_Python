import turtle
import random

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

pointer.speed("slow")
for position in range(4):
    pointer.forward(200)
    pointer.left(90)


pointer.clear()

pointer.speed("fastest")
for position in range(100):
    pointer.circle(100)
    pointer.setheading(pointer.heading() + 10)


pointer.clear()

pointer.up()
pointer.speed("slow")
for position in range(10):
    pointer.dot(20, random.choice(random_colors))
    pointer.forward(50)
    




scr.exitonclick()
