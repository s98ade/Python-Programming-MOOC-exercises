from collections import Counter

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequency = Counter(my_list)
        most_common_item, _ = frequency.most_common(1)[0]
        return most_common_item

    @classmethod
    def doubles(cls, my_list: list):
        frequency = Counter(my_list)
        count_doubles = sum(1 for item, count in frequency.items() if count >= 2)
        return count_doubles