import turtle
from random import randint, choice

class Turtler():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ws = turtle.Screen()
        self.ws.window_width = self.width
        self.ws.window_height = self.height

        self.ws.bgcolor('white')
        self.turtle = turtle.Turtle()

        self.turtle.penup()
        self.turtle.goto(
            0, 0
        )
        self.turtle.pendown()

        self.msg = 'placeholder'
    
    def draw_text(self, msg):
        self.turtle.reset()

        self.turtle.home()
        self.turtle.penup()

        self.turtle.sety(self.height-30)

        self.turtle.pencolor('black')

        self.turtle.pendown()
        self.turtle.write(
            msg, 
            move=False,
            align='center',
            font=('Arial', 20, 'normal')
        )

        self.turtle.penup()
    
    def draw_cornered(self, corners, length, corner):
        self.turtle.home()
        self.turtle.pendown()

        for _ in range(corners):
            self.turtle.right(corner)
            self.turtle.forward(length)
    
    def draw_cube(self):
        self.draw_cornered(
            4,
            100,
            90
        )
        
    def draw_circle(self):
        self.turtle.home()
        self.turtle.pendown()

        self.turtle.circle(
            randint(40, 100)
        )

if __name__ == '__main__':
    turd = Turtler(400, 400)

    '''

    turd.draw_text('Drawing cube')
    turd.turtle.pencolor('black')
    turd.draw_cube()

    turd.draw_text('Drawing circle')
    turd.turtle.pencolor('blue')
    turd.draw_circle()

    turd.draw_text('Drawing a triangle')
    turd.turtle.pencolor('purple')
    turd.draw_cornered(3, 60, 120)

    turd.draw_text('Drawing a pentagon')
    turd.turtle.pencolor('red')
    turd.draw_cornered(5, 40, 72)

    turd.draw_text('Drawing a hexagon')
    turd.turtle.pencolor('green')
    turd.draw_cornered(6, 40, 60)

    turd.draw_text('Drawing a decagon')
    turd.turtle.pencolor('pink')
    turd.draw_cornered(10, 40, 36)

    turd.draw_text('Drawing a star')
    turd.turtle.pencolor('black')
    turd.draw_cornered(5, 100, 144)

    for i in range(3):
        turd.draw_text(f'Drawing cube {i+1}')
        turd.turtle.width(randint(
            2, 10
        ))

        turd.turtle.pencolor(choice([
            'red',
            'blue',
            'green',
            'purple',
            'yellow'
        ]))

        turd.draw_cube()
    '''
    
    turd.draw_text('Drawing art!')
    for _ in range(5):
        turd.turtle.pencolor(choice([
            'red',
            'blue',
            'green',
            'purple',
            'yellow',
            'black',
            'pink'
        ]))

        turd.turtle.width(randint(1, 10))

        turd.draw_circle()

    input()