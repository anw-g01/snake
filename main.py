from gameplay import Game


def starting_segments():
    """Allows user to enter a starting number of snake segments to begin with."""
    while True:
        try:
            segments = int(input("\nEnter starting no. of segments (1-10): "))
            if segments in list(range(1, 11)):
                return segments
        except ValueError:
            print("Invalid input. Try again.")


def main():

    game = Game(starting_segments())

    while True:

        while True:
            game.configure_controls()       # listen for user input events
            game.scoreboard.display_score()     # display the current score

            game.snake.move()       # start moving the snake continuously until end-game scenarios
            game.detect_food_collision()    # increase score if user eats food

            game.update_screen()        # update the frame rate of the animation

            if game.game_over():    # check if snake hits boundary wall or its own body
                break   # end game loop (game over)

        if not game.play_again():   # user has the option to play again
            break
        else:
            game.reset_game()       # reset game settings if user wishes to play again
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
