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
pointer.hideturtle()
turtle.colormode(255)

#screen settings
scr = turtle.Screen()
scr.setup(width=500, height=500)

pointer.up()
pointer.goto(-125,-125)
pointer.speed("slow")
pointer.width(20)
pointer.down()



for position in range(4):
    pointer.forward(225)
    pointer.left(90)

time.sleep(3)
pointer.clear()


pointer.up()
pointer.speed("fastest")
pointer.goto(0,0)
pointer.width(1)
pointer.down()
for position in range(100):
    pointer.color(random.choice(random_colors))
    pointer.circle(100)
    pointer.setheading(pointer.heading() + 10)


pointer.clear()


pointer.up()
pointer.goto(-210,-210)
pointer.speed("fastest")
a = pointer.heading()
print(a)
pointer.left(360-a)
y = 20

for position in range(1, 199):
    pointer.dot(20, random.choice(random_colors))
    pointer.forward(50)
    
    if position % 9 == 0:
        pointer.goto(-210, -210 + y)
        y +=20
    




scr.exitonclick()
