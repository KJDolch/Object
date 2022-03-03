"""
Exercise 2 - Class Bike 2
"""
# Expand the class from the first exercise by adding several methods to it
class Bike:
    def __init__(self, brand, nr_sprockets, nr_pinion, sprocket, pinion):
        self.__brand = str(brand)
        self.__nr_sprockets = int(nr_sprockets)
        self.__nr_pinion = int(nr_pinion)
        self._sprocket = int(sprocket)
        self._pinion = int(pinion)

    # one getter() for each attribute defined in the class (get_brand() and so on)
    def get_brand(self, new_brand):
        if type(new_brand) == type(float()):
            raise ValueError("Only string allowed")
        elif type(new_brand) == type(int()):
            raise ValueError("Only string allowed")
        else:
            self.__brand = str(new_brand)

    def get_nr_sprockets(self, new_nr_sprockets):
        if type(new_nr_sprockets) == type(float()):
            raise ValueError("Only whole number allowed")
        elif type(new_nr_sprockets) == type(str()):
            raise ValueError("Only whole number allowed")
        else:
            self.__nr_sprockets = int(new_nr_sprockets)

    def get_nr_pinion(self, new_nr_pinion):
        if type(new_nr_pinion) == type(float()):
            raise ValueError("Only whole number allowed")
        elif type(new_nr_pinion) == type(str()):
            raise ValueError("Only whole number allowed")
        else:
            self.__nr_pinion = int(new_nr_pinion)

    def get_sprocket(self, new_sprocket):
        if type(new_sprocket) == type(float()):
            raise ValueError("Only whole number allowed")
        elif type(new_sprocket) == type(str()):
            raise ValueError("Only whole number allowed")
        else:
            self._sprocket = int(new_sprocket)

    def get_pinion(self, new_pinion):
        if type(new_pinion) == type(float()):
            raise ValueError("Only whole number allowed")
        elif type(new_pinion) == type(str()):
            raise ValueError("Only whole number allowed")
        else:
            self._pinion = int(new_pinion)

    # the methods up_sprockets(), down_sprocket(), up_pinion() and down_pinion() that allow the user to change the sprocket and pinion accordingly but only if possible

    def up_sprocket(self):
        if self._sprocket == self.__nr_sprockets:
            print("You already are in the biggest sprocket")
        else:
            self._sprocket += 1
            print("You're sprocket was increased.")

    def down_sprocket(self):
        if self._sprocket == 1:
            print("You already are in the lowest sprocket")
        else:
            self._sprocket -= 1
            print("You're sprocket was decreased.")

    def up_pinion(self):
        if self._pinion == self.__nr_pinion:
            print("You already are in the biggest pinion")
        else:
            self._pinion += 1
            print("You're pinion was increased.")

    def down_pinion(self):
        if self._pinion == 1:
            print("You already are in the lowest pinion")
        else:
            self._pinion -= 1
            print("You're pinion was decreased.")

    # last but not least create a method print_state() that prints out the name of the bike, the used sprocket and the used pinion
    def print_state(self):
        print("")
        print("The brand of your bike is", self.__brand)
        print(
            "You're currently at sprocket",
            self._sprocket,
            "of",
            self.__nr_sprockets,
            "sprockets",
        )
        print(
            "You're currently at pinion",
            self._pinion,
            "of",
            self.__nr_pinion,
            "pinions",
        )
        print("")


MyBike = Bike("Ich", 2, 10, 1, 1)
MyBike.up_sprocket()
MyBike.up_sprocket()
MyBike.down_sprocket()
MyBike.up_sprocket()
MyBike.print_state()
MyBike.down_pinion()
MyBike.up_pinion()
MyBike.up_pinion()
MyBike.up_pinion()
MyBike.print_state()
