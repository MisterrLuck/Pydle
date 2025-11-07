import random

class Pydle:
    def __init__(self):
        self.possible_words = ['games', 'fried', 'short', 'orate', 'audio']
        self.answer = []
        self.max_guesses = 6
        self.guesses = 0

    def reset(self):
        self.random_word()
        self.guesses = 0
    
    def print_answer(self):
        print(''.join(self.answer))

    def random_word(self):
        with open("wordlist.txt", "r") as file:
            lines = file.readlines()
            count = len(lines)
            ind = random.randint(0, count-1)
            self.answer = list(lines[ind].strip())

    def make_guess(self, word_guess: str) -> str:
        if len(word_guess) != 5:
            raise Exception("Only 5 letter guesses")

        list_guess = list(word_guess)
        answer_copy = self.answer.copy()
        if list_guess == self.answer:
            return "GGGGG"

        greens = []
        # Find the Greens
        for i in range(5):
            if list_guess[i] == answer_copy[i]:
                greens.append("G")
                list_guess[i] = "*"
                answer_copy[i] = "*"
            else:
                greens.append("-")
        
        yellows = []
        # Find the Yellows
        for char in list_guess:
            if char in answer_copy:
                answer_copy.remove(char)
                yellows.append("Y")
            else:
                yellows.append("-")
                    
        self.guesses += 1
        return ''.join(self.union(greens, yellows))
    
    def union(self, first: list[str], second: list[str]) -> list[str]:
        if len(first) != len(second) or len(first) != 5:
            raise Exception("Only 5 letter guesses")
        unioned = []
        for i in range(5):
            if first[i] == "G" or second[i] == "G":
                unioned.append("G")
            elif first[i] == "Y" or second[i] == "Y":
                unioned.append("Y")
            else:
                unioned.append("-")
        return unioned
