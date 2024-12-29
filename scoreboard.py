from turtle import Turtle

class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 1
        self.FONT = ("Courier", 24, "normal")
        self.level = Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.goto(-220, 250)
        self.level.color('black')
        self.update_level()

    def update_level(self):
        self.level.clear()
        self.level.write(f'Level :{self.score}', align='center', font=self.FONT)

    def next_level(self):
        print('You made it!')
        self.score += 1

    def game_over(self):
        game_over_text = Turtle()
        game_over_text.hideturtle()
        game_over_text.write('GAME OVER', align='center', font=self.FONT)
