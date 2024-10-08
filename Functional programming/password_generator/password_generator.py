import random
import string

def generate_strong_password(char_amount: int, include_numbers: bool, include_special_chars: bool) -> str:
    password = ""
    
    if not include_numbers and not include_special_chars:
        characters = string.ascii_lowercase
    else:
        characters = string.ascii_letters + (string.digits if include_numbers else '') + ("!?=+-()#" if include_special_chars else '')
    
    password += random.choice(string.ascii_lowercase)  # Ensure at least one lowercase alphabet
    char_amount -= 1
    
    if include_numbers:
        password += random.choice(string.digits)
        char_amount -= 1
    
    if include_special_chars:
        password += random.choice("!?=+-()#")
        char_amount -= 1
    
    for i in range(char_amount):
        password += random.choice(characters)
        
    password = ''.join(random.sample(password, len(password)))  # Shuffle characters
    
    return password.lower()

if __name__ == "__main__":
    for i in range(3):
        print(generate_strong_password(6, False, False))