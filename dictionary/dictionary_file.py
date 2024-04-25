# Write your solution here
def add_word():
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    with open("dictionary.txt", "a") as file:
        file.write(f"{finnish_word}:{english_word}\n")
    print("Dictionary entry added")

def search_word():
    search_term = input("Search term: ")
    with open("dictionary.txt", "r") as file:
        for line in file:
            if ":" in line:
                finnish, english = line.strip().split(":")
                if search_term.lower() in finnish.lower() or search_term.lower() in english.lower():
                    print(f"{finnish} - {english}")

def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        if function == 1:
            add_word()
        elif function == 2:
            search_word()
        elif function == 3:
            print("Bye!")
            break

main()