from pydle import Pydle


game = Pydle()
game.reset()
# game.answer = list("karek")
# print(game.answer)
# game.print_answer()
while game.guesses < game.max_guesses:
    guess = input("> ")
    result = game.make_guess(guess)
    print("= "+result)
    if result == "GGGGG":
        print("Congrats")
        break
if result != "GGGGG":
    print("Oh well")