from pydle import Pydle


game = Pydle()
game.reset()
game.answer = "karek"
print(game.answer)
guess = input("> ")
print("result: "+game.make_guess(guess))