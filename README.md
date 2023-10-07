# Snake

A classic arcade game built in Python using the Turtle graphics library.

## Project Files
1. `main.py`: Main script that initialises the game and handles the main game logic.
2. `config.py`: Stores configuration parameters (global variables) for the game, allowing custimisation across nearly every aspect.
3. `gameplay.py`: Manages the main game logic by handling wall and segment collision as well as the snake eating food.
4. `classes.py`: Contains definitions of classes to represent the snake, body segments, food and the scoreboard.
5. `high_score.txt`: Text file that stores the all-time high score for the game to keep track in memory.

# How to play
1. Run `main.py` to start the program.
2. The program allows you to enter the number of starting snake segments, which is how long you want the snake to be when the game first starts.
3. Use the arrow keys on your keyboard to control the snake in all directions. The snake cannot move back in the opposite direction (do a 180 degree turn).
4. Eat the foods (coloured circles) as they appear on the screen to increase your score by colliding into them.
5. Avoid hitting the walls (edges of the screen) or the snake's own body segments otherwise it is game over.
6. You can choose to keep playing again or exit the main program.
