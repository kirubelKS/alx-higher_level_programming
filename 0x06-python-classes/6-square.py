#!/urs/bin/python3

"""Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size (int): the size of the new square.
            position (int, int): the position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set the current size of the square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an ingeger")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get/set the current position of the square."""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
                 len (value) != 2 or 
                not all(isinstance(num, int) for num in value)or 
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive ingegers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        
        [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ",end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
            