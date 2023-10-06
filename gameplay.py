from turtle import Screen
from classes import Snake, Food, Scoreboard
from config import *
import time


def make_screen():
    """Initialise the Screen() object from the turtle module for the game window."""
    screen = Screen()
    screen.bgcolor(SCREEN_COLOUR)
    screen.title("Snake")
    screen.setup(
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT
    )
    screen.tracer(0)
    return screen


class Game:
    """
    Represents the snake game and houses the main game logic for calling methods.

    attributes:
    screen - instantiates a Screen() object from the turtle class
    snake - instantiates a Snake() object from classes.py to represent the player's controlling character
    scoreboard - instantiates a Scoreboard() from classes.py object to call text displaying methods
    """
    def __init__(self, starting_segments):
        self.screen = make_screen()
        self.snake = Snake(starting_segments)
        self.food = Food()
        self.scoreboard = Scoreboard()

    def update_screen(self):
        """Updates the screen with the next frame of the game animation using TIME_STEP increments."""
        self.screen.update()
        time.sleep(TIME_STEP)

    def configure_controls(self):
        """Configures keybindings for controlling the snake."""
        self.screen.listen()
        self.screen.onkey(self.snake.head_north, "Up")
        self.screen.onkey(self.snake.head_south, "Down")
        self.screen.onkey(self.snake.head_west, "Left")
        self.screen.onkey(self.snake.head_east, "Right")

    def detect_food_collision(self):
        """Detects when the snake eats the food object by colliding with it."""
        if self.snake.head.distance(self.food) < (FOOD_DIAMETER / 2) + (SEGMENT_SIDE_LENGTH / 2):
            self.food.new_position()
            self.scoreboard.update_score()
            self.snake.add_segment()

    def game_over(self):
        """Detects whether the snake hits the screen boundaries or its own body segment to end the game."""
        if self.snake.wall_collision() or self.snake.segment_collision():
            self.food.hideturtle()      # hides the food object as a visual
            self.screen.update()        # update hiding the food
            self.scoreboard.display_game_over()     # displays game over and final score
            return True
        return False

    def play_again(self):
        """Prompts the user if they wish to play a new game."""
        while True:
            ans = self.screen.textinput(
                title="Game Over",
                prompt="Play again? (y/n)?"
            ).lower()
            if ans in ["y", "n"]:
                return ans == "y"
            print("Invalid input. Try again.")

    def reset_game(self):
        """Resets the position of the snake, scoreboard and food position."""
        self.snake.reset_snake()
        self.scoreboard.reset_score()
        self.food.showturtle()
        self.food.new_position()
