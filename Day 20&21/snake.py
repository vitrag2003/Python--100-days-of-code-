from turtle import Turtle

starting_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        # segment1=Turtle("square")
        # segment1.color("white")

        # segment2=Turtle("square")
        # segment2.color("white")
        # segment2.penup()
        # segment2.goto(x=-20,y=0)

        # segment3=Turtle("square")
        # segment3.color("white")
        # segment3.penup()
        # segment3.goto(x=-40,y=0)

        # segments.append(segment1)
        # segments.append(segment2)
        # segments.append(segment3)

        for position in starting_positions:  #this for loops creates the snake
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def reset_game(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.segments)-1,0,-1): #This for loop: moves the snake forward ; range(start=2,stop=0,step=-1) this is for loop for reverse iteration
            new_x=self.segments[seg_num-1].xcor() 
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)

    