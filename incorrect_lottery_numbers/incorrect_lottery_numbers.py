# Write your solution here
import csv

def is_valid_line(line) -> bool:
    parts = line.strip().split(';')
    if len(parts) != 2:
        return False
    
    week_number, numbers = parts
    if not week_number.startswith("week ") or not week_number[5:].isdigit():
        return False
    
    numbers = numbers.split(',')
    if len(numbers) != 7:
        return False
    
    for num in numbers:
        try:
            num_int = int(num)
            if num_int < 1 or num_int > 39:
                return False
        except ValueError:
            return False
        if numbers.count(num) > 1:
            return False
    
    return True

def filter_incorrect():
    with open('lottery_numbers.csv', 'r') as input_file, \
         open('correct_numbers.csv', 'w', newline='') as output_file:

        reader = csv.reader(input_file, delimiter=';')
        writer = csv.writer(output_file, delimiter=';')

        for row in reader:
            if len(row) == 2 and is_valid_line(';'.join(row)):
                writer.writerow(row)
