class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError("Length cannot be negative.")
        self.__length = length

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Length shouldn't be a negative value.")
        
if __name__ == "__main__":
    the_wall = Recording(-1)
    print(the_wall.length)
    the_wall.length = -1
    print(the_wall.length)