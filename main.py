from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class Main:
    def __init__(self):
        # Setup window specs
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title('Turtle Crossing')
        self.screen.listen()
        self.screen.tracer(0)

        # Call modules/ functions
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.controls()

        # Declare variables
        self.game_is_on = True

    def controls(self):
        # Listen key controls
        self.screen.onkey(self.player.crawl, 'Up')
        self.screen.onkey(self.end, 'Escape')
        self.screen.onkey(self.restart, 'Return')

    def restart(self):
        # Restarts the game
        print('Restart')
        self.game_is_on = True
        self.scoreboard.restart()
        self.scoreboard.update_level()
        self.car_manager.restart()
        self.player.go_to_start()
        self.run()

    def end(self):
        # End game by pressing ESC key
        self.screen.bye()

    # Main function to run game
    def run(self):
        while self.game_is_on:
            try:
                sleep(0.1)
            except ValueError:
                print('Value turned negative! Resetting to base speed')

            self.car_manager.create_car()
            self.car_manager.move_car()

            # Detect collisions of turtle to crossing cars
            for car in self.car_manager.all_cars:
                if self.player.distance(car) < 20:
                    self.game_is_on = False
                    self.scoreboard.game_over()

            # Detect if turtle made it to the finish line
            if self.player.is_at_finish_line():
                self.scoreboard.next_level()
                self.scoreboard.update_level()
                self.car_manager.speed_up()

            self.screen.update()
        self.screen.exitonclick()


if __name__ == "__main__":
    game = Main()
    game.run()
