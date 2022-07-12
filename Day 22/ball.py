from turtle import Turtle 

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move*=-1      #reversing the direction of the ball vertically
        
    def bounce_x(self):
        self.x_move*=-1      #reversing the direction of the ball horizontally
        self.move_speed *= 0.75

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x() #when the right paddle misses and the game restarts the ball will move towards the opposite paddle as he as won the earlier round
        
