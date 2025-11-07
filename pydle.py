import random

class Pydle:
    def __init__(self):
        self.possible_words = ['games', 'fried', 'short', 'orate', 'audio']
        self.answer = None
        self.max_guesses = 6
        self.guesses = 0
    
    def reset(self):
        self.random_word()
        self.guesses = 0

    def random_word(self):
        self.answer = random.choice(self.possible_words)

    def make_guess(self, word_guess: str) -> str:
        if len(word_guess) != 5:
            raise Exception("Only 5 letter guesses")
        if word_guess == self.answer:
            return "GGGGG"

        dups = ""
        for i in range(5):
            count = word_guess.count(word_guess[i])
            if count > 0 :
                dups += word_guess[i]


        greens = ""
        # Find the Greens
        for i in range(5):
            if word_guess[i] == self.answer[i]:
                greens += "G"
            else:
                greens += "-"
        
        yellows = ""
        # Find the Yellows
        for i in range(5):
            if word_guess[i] in self.answer:
                if word_guess.count(word_guess[i]) == self.answer.count(word_guess[i]):
                    yellows += "Y"
                else:
                    yellows += "P"
            else:
                yellows += "-"
                    
        self.guesses += 1
        return self.union(greens, yellows)
    
    def union(self, first: str, second: str):
        print("first:  "+first)
        print("second: "+second)
        if len(first) != len(second) or len(first) != 5:
            raise Exception("Only 5 letter guesses")
        unioned = ""
        for i in range(5):
            if first[i] == "G" or second[i] == "G":
                unioned += "G"
            elif first[i] == "Y" or second[i] == "Y":
                unioned += "Y"
            else:
                unioned += "-"
        return unioned