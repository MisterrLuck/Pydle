import random

class Pydle:
    def __init__(self):
        self.possible_words = ['games', 'fried', 'short', 'orate', 'audio']
        self.answer = []
        self.max_guesses = 6
        self.guesses = 0
    
    def from_word_list(self):
        with open("wordlist.txt", "r") as file:
            file.readlines

    def reset(self):
        self.random_word()
        self.guesses = 0
    
    def print_answer(self):
        print(''.join(self.answer))

    def random_word(self):
        self.answer = list(random.choice(self.possible_words))

    def make_guess(self, word_guess: str) -> str:
        if len(word_guess) != 5:
            raise Exception("Only 5 letter guesses")

        list_guess = list(word_guess)
        answer_copy = self.answer.copy()
        if list_guess == self.answer:
            return "GGGGG"

        # dups = ""
        # for i in range(5):
        #     count = word_guess.count(word_guess[i])
        #     if count > 0 :
        #         dups += word_guess[i]

        # print(list_guess)
        # print(self.answer)

        greens = []
        # Find the Greens
        for i in range(5):
            if list_guess[i] == answer_copy[i]:
                greens.append("G")
                list_guess[i] = "*"
                answer_copy[i] = "*"
            else:
                greens.append("-")

        # print(f"Guess:  {list_guess}")
        # print(f"Answer: {answer_copy}")
        
        
        yellows = []
        # Find the Yellows
        for char in list_guess:
            if char in answer_copy:
                # print(f"bef answer: {answer_copy}")
                # print(f"bef guess: {list_guess}")
                # print(f"bef yellow: {yellows}")
                # print(f"char: {char}")
                answer_copy.remove(char)
                # list_guess.remove(char)
                # if list_guess.count(list_guess[i]) == answer_copy.count(list_guess[i]):
                yellows.append("Y")
                # print(f"aft answer: {answer_copy}")
                # print(f"aft guess: {list_guess}")
                # print(f"aft yellow: {yellows}")
                # print()
                # else:
                #     yellows.append("D")
            else:
                # print(f"aft yellow: {yellows}")
                yellows.append("-")
                # print(f"aft yellow: {yellows}")
                # print()
                    
        self.guesses += 1
        return ''.join(self.union(greens, yellows))
    
    def union(self, first: list[str], second: list[str]) -> list[str]:
        # print("first:  "+ ''.join(first))
        # print("second: "+''.join(second))
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