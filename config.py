# ====== GAME WINDOW ====== #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOUR = "black"

# ====== ANIMATION ====== #
TIME_STEP = 0.08

# ====== FOOD ====== #
FOOD_DIAMETER = 12
FOOD_COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]

# ====== SNAKE BODY ====== #
SEGMENT_COLOUR = "white"
SEGMENT_SIDE_LENGTH = 15
MOVE_DISTANCE = SEGMENT_SIDE_LENGTH
STARTING_SEGMENTS = 3
SEGMENT_GAP = 3

# ====== TEXT DISPLAY ====== #
TEXT_COLOUR = "white"
ALIGNMENT = "center"
FONT_NAME = "Courier New"
FONT_STYLE = "normal"
FONT_SIZE = 20
FONT = (FONT_NAME, FONT_SIZE, FONT_STYLE)
UPDATE_SCORE_LAG = 0.1      # set to 0 for no animation pause when food is eaten
