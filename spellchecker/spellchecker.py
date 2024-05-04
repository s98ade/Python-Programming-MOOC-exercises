# write your solution here
# out of curiosity checking how many words in file
# with open("wordlist.txt", 'r') as file:
#    words = len(file.readlines())
#    print(words)

import difflib

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = set(file.read().split())
    return words

def spell_check(text, dictionary):
    words = text.split()

    corrected_text = []
    suggestions = {}

    for word in words:
        if word.lower() in dictionary:
            corrected_text.append(word)
        else:
            suggestions[word] = difflib.get_close_matches(word, dictionary)

            if suggestions[word]:
                corrected_text.append(f"*{word}*")
            else:
                corrected_text.append(word)

    corrected_text = ' '.join(corrected_text)
    return corrected_text, suggestions

def main():
    dictionary_file = 'wordlist.txt'
    dictionary = load_dictionary(dictionary_file)

    text = input("write text: ")

    corrected_text, suggestions = spell_check(text, dictionary)
    print(corrected_text)

    print("suggestions:")
    for misspelled_word, suggestion_list in suggestions.items():
        if suggestion_list:
            print(f"{misspelled_word}: {', '.join(suggestion_list)}")

main()