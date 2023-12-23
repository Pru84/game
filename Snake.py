from turtle import Screen, Turtle
S_P=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for p in S_P:
            new_seg=Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(p)
            self.segments.append(new_seg)

    def extend(self):
        new_seg=Turtle("square")
        new_seg.color("red")
        new_seg.penup()
        new_seg.goto(self.segments[-1].position())
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)