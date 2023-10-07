from turtle import Turtle
from config import *
import random
import time


class Segment(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent a snake body segment.

    attributes (all inherited):
    color -  colour of the segment
    shapesize - set the height and length of a square segment using SEGMENT_SIDE_LENGTH
    """
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color(SEGMENT_COLOUR)
        self.shapesize(
            stretch_wid=SEGMENT_SIDE_LENGTH/20,
            stretch_len=SEGMENT_SIDE_LENGTH/20
        )


class Snake:
    """
    Represents the snake in the game - a collection of single file Segment() objects.

    attributes:
    starting_segments (int) - the initial number of segments the snake starts with, set by user input.
    all_segments (list) - a list to store all segment objects of the snake.
    head (Segment): the first segment object in the all_segments stack, represents the head of the snake.
    """
    def __init__(self, starting_segments):
        self.starting_segments = starting_segments      # start game with starting no. of segments
        self.all_segments = []
        self.starting_snake()
        self.head = self.all_segments[0]    # assign head as first segment in the main list

    def starting_snake(self):
        """Initialises the snake with specified number of starting segments."""
        shift = 0
        for _ in range(self.starting_segments):
            segment = self.new_segment()
            segment.setpos(0 - shift, 0)
            shift += SEGMENT_SIDE_LENGTH + SEGMENT_GAP

    def reset_snake(self):
        """Resets the number of snake segments back to the starting number for a new game."""
        for segment in self.all_segments:
            segment.clear()
            segment.hideturtle()
        self.all_segments = []
        self.starting_snake()
        self.head = self.all_segments[0]

    def new_segment(self):
        """Instantiates and returns a new segment object."""
        seg = Segment()
        self.all_segments.append(seg)
        return seg

    def add_segment(self):
        """
        Adds a new segment object to the tail-end of the snake. If snake starts off with one starting segment, the new
        segment is positioned manually according to the direction of the moving snake - this is to prevent a trigger
        of segment_collision() as the head of the snake would also be its tail. Otherwise, place position of the new
        segment at the position of the tail. The segment will move and separate accordingly to the move() method logic.
        """
        tail = self.all_segments[-1]  # last segment in the list
        seg = self.new_segment()
        self.all_segments.append(seg)
        if self.starting_segments == 1:     # if user starts with one snake segment; prevents triggering collision logic
            dist = SEGMENT_SIDE_LENGTH + SEGMENT_GAP
            if self.head.heading() == 90:   # heading north
                seg.goto(tail.xcor(), tail.ycor() - dist)
            elif self.head.heading() == 270:    # heading south
                seg.goto(tail.xcor(), tail.ycor() + dist)
            elif self.head.heading() == 0:  # heading east
                seg.goto(tail.xcor() - dist, tail.ycor())
            elif self.head.heading() == 180:    # heading west
                seg.goto(tail.xcor() + dist, tail.ycor())
        else:
            seg.goto(tail.position())   # for more than 2 segments, new segment goes to tail location

    def move(self):
        """
        Updates the position of each segment based on the position of the segment in front of it. Starting from the
        last segment and iteratively updating the position for each segment until it reaches the head of the snake
        (the first segment). Finally, the head segment is moved forward by a fixed distance to simulate the movement
        of the snake.
        """
        for i in range(len(self.all_segments) - 1, 0, -1):
            seg = self.all_segments[i]
            pos_in_front = self.all_segments[i - 1].position()
            seg.goto(pos_in_front)
        self.head.forward(MOVE_DISTANCE + SEGMENT_GAP)

    def segment_collision(self):
        """Detects if the head of the snake collides with any other segment along its body."""
        for i in range(1, len(self.all_segments)):
            seg = self.all_segments[i]
            if self.head.distance(seg) < SEGMENT_SIDE_LENGTH / 2:
                return True
        return False

    def wall_collision(self):
        """Detects if the head of the snake collides with any of the screen window boundaries."""
        return (abs(self.head.xcor()) > (SCREEN_WIDTH / 2 - SEGMENT_SIDE_LENGTH) or
                abs(self.head.ycor()) > (SCREEN_HEIGHT / 2 - SEGMENT_SIDE_LENGTH))

    def head_north(self):
        """Directs the movement of the snake to go upwards."""
        if self.head.heading() != 270:  # if not south
            self.head.setheading(90)

    def head_south(self):
        """Directs the movement of the snake to go downwards."""
        if self.head.heading() != 90:   # if not north
            self.head.setheading(270)

    def head_west(self):
        """Directs the movement of the snake to go left."""
        if self.head.heading() != 0:    # if not east
            self.head.setheading(180)

    def head_east(self):
        """Directs the movement of the snake to go right."""
        if self.head.heading() != 180:  # if not west
            self.head.setheading(0)


class Food(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent food in the snake game.
    """
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(
            stretch_wid=FOOD_DIAMETER / 20,
            stretch_len=FOOD_DIAMETER / 20
        )
        self.new_position()

    def new_position(self):
        """Sets a random colour for the food and randomly positions it within the game window screen."""
        self.clear()
        self.color(random.choice(FOOD_COLOURS))
        rand_x = random.randint(-SCREEN_WIDTH / 2 + 2*FOOD_DIAMETER, SCREEN_WIDTH / 2 - 2*FOOD_DIAMETER)
        rand_y = random.randint(-SCREEN_HEIGHT / 2 + 2*FOOD_DIAMETER, SCREEN_HEIGHT / 2 - 2*FOOD_DIAMETER)
        self.goto(rand_x, rand_y)


class Scoreboard(Turtle):
    """
    Inherits the Turtle class from the turtle module to display text as the scoreboard.

    non-inherited attributes:
    score - the number of foods eaten by the snake in a game played by the user
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0  # how many foods eaten
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

    def reset_score(self):
        """Resets the score back to zero."""
        self.score = 0

    def update_score(self):
        """Increases the score by one with a "+1" animation and time lag at the centre of the screen."""
        self.score += 1
        self.goto(0, 0)
        self.write(
            "+1",
            align="center",
            font=(FONT_NAME, 30, FONT_STYLE),
        )
        time.sleep(UPDATE_SCORE_LAG)

    def display_score(self):
        """Displays the score value at the top of the screen displaying."""
        self.clear()
        self.goto(0, SCREEN_HEIGHT / 2 - 40)
        self.write(
            f"YOUR SCORE: {self.score} (HIGH SCORE: {self.high_score})",
            align="center",
            font=FONT,
        )

    def display_high_score(self, new=False):
        """Displays the all-time high score value when the game is over. Also displays if it is a new high score."""
        self.goto(0, SCREEN_HEIGHT / 2 - 80)
        if new:
            self.write(
                f"NEW HIGH SCORE: {self.high_score}",
                align="center",
                font=FONT,
            )
        else:
            self.write(
                f"ALL-TIME HIGH SCORE: {self.high_score}",
                align="center",
                font=FONT,
            )

    def update_high_score(self):
        """Updates and stores the all-time high-score in a text file."""
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
                self.high_score = self.score
            self.display_high_score(new=True)   # display a new high score
        else:
            self.display_high_score()   # display the all-time standing high score

    def reset_high_score(self):
        """Resets the all-time high score back to 0."""
        with open("high_score.txt", "w") as file:
            file.write("0")
            self.high_score = int(file.read())

    def display_game_over(self):
        """Displays a game over message and presents the final achieved score value."""
        self.clear()
        self.goto(0, SCREEN_HEIGHT / 4)
        self.write(
            f"GAME OVER",
            align="center",
            font=(FONT_NAME, FONT_SIZE, "bold")
        )
        self.goto(0, -40 + SCREEN_HEIGHT / 4)
        self.write(
            f"SCORE: {self.score}",
            align="center",
            font=FONT
       )


