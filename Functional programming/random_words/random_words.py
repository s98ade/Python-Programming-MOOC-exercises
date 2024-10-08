# Write your solution here
import random

def words(n: int, beginning: str) -> list[str]:
    # Read words from the file and filter those beginning with the specified string
    with open("words.txt", "r") as file:
        all_words = [word.strip() for word in file if word.startswith(beginning)]
    
    if len(all_words) < n:
        raise ValueError("Not enough words beginning with the specified string.")
    
    # Randomly select n unique words from the filtered list
    selected_words = random.sample(all_words, n)
    
    return selected_words

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
