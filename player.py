from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.left(90)
        self.go_to_start()

    def crawl(self):
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        # Detect if turtle made it to finish line
        if self.ycor() > 280:
            self.go_to_start()
            return True
        else:
            return False

    def go_to_start(self):
        # Turtle returns back to starting position
        self.goto(self.STARTING_POSITION)




