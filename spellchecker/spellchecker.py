# write your solution here
# out of curiosity checking how many words in file
# with open("wordlist.txt", 'r') as file:
#    words = len(file.readlines())
#    print(words)

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = set(file.read().split())
    return words

def spell_check(text, dictionary):
    words = text.split()

    corrected_text = []
    for word in words:
        if word.lower() in dictionary:
            corrected_text.append(word)
        else:
            corrected_text.append(f"*{word}*")

    corrected_text = ' '.join(corrected_text)
    return corrected_text

def main():
    dictionary_file = 'wordlist.txt'
    dictionary = load_dictionary(dictionary_file)

    text = input("Write text: ")

    corrected_text = spell_check(text, dictionary)
    print(corrected_text)

main()