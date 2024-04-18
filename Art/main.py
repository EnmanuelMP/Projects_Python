import turtle
import random
import time
# Function to generate random RGB color tuples
def generate_random_color(Color_Amount:int = 100):
    Colors =[
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ) 
        for _ in range(Color_Amount)
    ]

    return Colors


def set_pointer(pointer:turtle,position:tuple = (0,0), speed:str = "slow", width:float = 1, draw:bool = True):
    pointer.up()
    pointer.goto(position)
    pointer.speed(speed)
    pointer.width(width)
    if draw: pointer.down() 
    else: pointer.up()
    
    time.sleep(2)
    pointer.clear()


def main():
    # SETTINGS
        
        #Turtle
    pointer = turtle.Turtle()
    pointer.hideturtle()
    turtle.colormode(255)


        #Screen
    scr = turtle.Screen()
    scr.setup(width=500, height=500)

        #Assets
    random_colors:list = generate_random_color()



    #STARTING PROGRAM

    set_pointer(pointer,(-125,-125),"slow",20,True)

    for position in range(4):
        pointer.forward(225)
        pointer.left(90)


    set_pointer(pointer,(0,0),"fastest",1,True)

    for position in range(100):
        pointer.color(random.choice(random_colors))
        pointer.circle(100)
        pointer.setheading(pointer.heading() + 10)


    set_pointer(pointer,(-210,-210),"fastest",1,False)


    a = pointer.heading()
    pointer.left(360-a)
    y = 20

    for position in range(1, 199):
        pointer.dot(20, random.choice(random_colors))
        pointer.forward(50)
        
        if position % 9 == 0:
            pointer.goto(-210, -210 + y)
            y +=20
        


    scr.exitonclick()

if __name__ == '__main__':
    main()