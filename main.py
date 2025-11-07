from pydle import Pydle

if __name__ == "__main__":
    game = Pydle()
    game.reset()
    while game.guesses < game.max_guesses:
        guess = input(f"{game.max_guesses-game.guesses}> ")
        result = game.make_guess(guess)
        print("== "+result)
        if result == "GGGGG":
            print("Congrats")
            break
    if result != "GGGGG":
        print("Oh well")
        print("\n< ", end="")
        game.print_answer()
