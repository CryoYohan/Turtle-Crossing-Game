from turtle import Turtle

class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 1
        self.FONT = ("Courier", 24, "normal")
        self.level = Turtle()
        self.game_over_text = Turtle()
        self.game_over_text.hideturtle()
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
        self.game_over_text.write('GAME OVER', align='center', font=self.FONT)

    def restart(self):
        self.game_over_text.clear()
        self.score = 1


