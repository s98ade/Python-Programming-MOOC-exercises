class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__number = []
        self.__address = None
    
    
    def add_number(self, number: int):
        self.__number.append(number)


    def add_address(self, address: str):
        self.__address = address
    
    
    def name(self):
        if self.__name is None:
            return None
        return self.__name
    
    
    def numbers(self):
        return self.__number
    
    
    def address(self):
        return self.__address 


    def __str__(self):
        result = f"{self.__name}\n"
        if self.__numbers:
            for number in self.__numbers:
                result += f"{number}\n"
        else:
            result += "number unknown\n"
        
        result += self.address()
        return result


class PhoneBook:
    def __init__(self):
        self.__persons = {}


    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)


    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)


    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]


    def all_entries(self):
        return self.__persons
    
    
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()


    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")


    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)


    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)


    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person is None:
            print("number unknown\naddress unknown")
        else:
            print(person)       


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


application = PhoneBookApplication()
application.execute()