class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self._max_weight = max_weight  
        self._items = []  
    
    def add_item(self, item: Item):
        current_weight = sum(i.weight() for i in self._items)
        
        if current_weight + item.weight() <= self._max_weight:
            self._items.append(item)

    def print_items(self):
        for i in self._items:
            print(i)

    def weight(self):
        return sum(i.weight() for i in self._items)
    
    def heaviest_item(self):
        if not self._items:
            return None
        return max(self._items, key=lambda item: item.weight())
    
    def __str__(self):
        total_weight = sum(item.weight() for item in self._items)
        item_str = "item" if len(self._items) == 1 else "items"

        return f"{len(self._items)} {item_str} ({total_weight} kg)"
    
class CargoHold:
    def __init__(self, max_weight:int):
        self._max_weight = max_weight
        self._suitcases = []

    def add_suitcase(self, suitcase: "Suitcase"):
        current_weight = sum(s.weight() for s in self._suitcases)
        
        if current_weight + suitcase.weight() <= self._max_weight:
            self._suitcases.append(suitcase)
    
    def print_items(self):
        for s in self._suitcases:
            s.print_items()

    def __str__(self):
        current_max_weight = self._max_weight - sum(s.weight() for s in self._suitcases)
        suitcase_str = "suitcase" if len(self._suitcases) == 1 else "suitcases"

        return f"{len(self._suitcases)} {suitcase_str}, space for {current_max_weight} kg"
    
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()