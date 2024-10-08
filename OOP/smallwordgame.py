import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word: str) -> int:
        # Define vowels
        vowels = "aeiouAEIOU"
        # Count and return the number of vowels in the word
        return sum(1 for char in word if char in vowels)

    def round_winner(self, player1_word: str, player2_word: str):
        # Count the vowels in both players' words
        vowels1 = self.count_vowels(player1_word)
        vowels2 = self.count_vowels(player2_word)

        # Determine the winner based on the number of vowels
        if vowels1 > vowels2:
            return 1
        elif vowels2 > vowels1:
            return 2
        
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = ['rock', 'paper', 'scissors']

        # If both inputs are invalid, it's a tie
        if player1_word not in valid_moves and player2_word not in valid_moves:
            print("Invalid inputs from both players. It's a tie.")
            return 0  # tie

        # If player1's input is invalid, player2 wins
        if player1_word not in valid_moves:
            print("Player 1 entered an invalid move.")
            return 2

        # If player2's input is invalid, player1 wins
        if player2_word not in valid_moves:
            print("Player 2 entered an invalid move.")
            return 1

        # If both inputs are valid, determine the winner based on rules
        if player1_word == player2_word:
            print("It's a tie.")
            return 0  # tie

        if (player1_word == 'rock' and player2_word == 'scissors') or \
           (player1_word == 'scissors' and player2_word == 'paper') or \
           (player1_word == 'paper' and player2_word == 'rock'):
            return 1  # player 1 wins
        else:
            return 2
        

if __name__ == "__main__":
    p = RockPaperScissors(1)
    p.play()