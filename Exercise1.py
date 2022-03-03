"""
Exercise 1 - Class Bike
"""

# generate your own class called "Bike" that has the following five attributes:
# __brand: a string (private)
# __nr-sprockets: a positive whole number (private)
# __nr_pinion: a positive whole number (private)
# _sprocket: a positive whole number (protected)
# _pinion: a positive whole number (protected)

# all attributes should be given to the constructor of the class if a new object is generated


class Bike:
    def __init__(self, brand, nr_sprockets, nr_pinion, sprocket, pinion):
        self.__brand = str(brand)
        self.__nr_sprockets = int(nr_sprockets)
        self.__nr_pinion = int(nr_pinion)
        self._sprocket = int(sprocket)
        self._pinion = int(pinion)


x = Bike("Kettler", 3, 2, 5, 6)
print(x._pinion)
print(x._sprocket)

# private attribute: can't be accessed, so no printout in the terminal
# protected attribute: can be accessed, but should not be changed.
