class Animal:
    """
    A class used to represent an animal
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """initilize Animal's class
        :param name: name of animal
        :param hunger: hunger level of each animal
        :type name: str
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """:return to program the name for the specific animal
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """:return bool for hunger level of each animal
        :rtype: bool
        """
        return True if self._hunger > 0 else False

    def feed(self):
        """feed animal by subtract 1 from hunger level.

        """
        self._hunger -= 1

    def talk(self):
        """list of talking options for each animal
        :type: list
        """
        self.talk = ["woof woof", "meow", "tsssss", "Good day, darling", "Raaaawr"]

class Dog(Animal):
    """
    A subclass(Animal) used to represent a dog
    """

    def __init__(self, name, hunger=0):
        """initilize Dog's class
        :param name: name of dog
        :param hunger: hunger level of each dog
        :type name: str
        :type hunger: int
        """
        Animal.__init__(self, name, hunger)

    def talk(self):
        """print to screen dog's talking option from Animal.talk()
        :return None but print to screen
        """
        super().talk()
        print(self.talk[0])

    def fetch_stick(self):
        """ Special power of each dog has
        :return None but print to program
        """
        print("There you go, sir!	")

class Cat(Animal):
    """
    A subclass(Animal) used to represent a cat
    """
    def __init__(self, name, hunger=0):
        """initilize Cat's class
        :param name: name of cat
        :param hunger: hunger level of each cat
        :type name: str
        :type hunger: int
        """
        Animal.__init__(self, name, hunger)

    def talk(self):
        """print to screen cat's talking option from Animal.talk()
        :return None but print to screen
        """
        super().talk()
        print(self.talk[1])

    def chase_laser(self):
        """ Special power of each cat has
        :return None but print to program
        """
        print("Meeeeow")

class Sknuk(Animal):
    """
    A subclass(Animal) used to represent a Sknuk
    """
    def __init__(self, name, hunger=0):
        """initilize Skuk's class
        specialAttribute: stink_count
        :attribute type: int
        :param name: name of sknuk
        :param hunger: hunger level of each sknuk
        :type name: str
        :type hunger: int

        """
        Animal.__init__(self, name, hunger)
        self._stink_count = 6

    def talk(self):
        """print to screen Sknuk's talking option from Animal.talk()
        :return None but print to screen
        """
        super().talk()
        print(self.talk[2])

    def stink(self):
        """ Special power of each Sknuk has
        :return None but print to program
        """
        print("Dear lord!")

class Unicorn(Animal):
    """
    A subclass(Animal) used to represent an unicorn
    """
    def __init__(self, name, hunger=0):
        """initilize unicorn's class
        :param name: name of unicorn
        :param hunger: hunger level of each unicorn
        :type name: str
        :type hunger: int
        """
        Animal.__init__(self, name, hunger)

    def talk(self):
        """print to screen Unicorn's talking option from Animal.talk()
        :return None but print to screen
        """
        super().talk()
        print(self.talk[3])

    def sing(self):
        """ Special power of each Unicorn has
        :return None but print to program
        """
        print("I’m not your toy...")

class Dragon(Animal):
    """
    A subclass(Animal) used to represent a dragon
    """
    def __init__(self, name, hunger=0):
        """initilize dragon's class
        specialAttribute: _color
        Attribute type: str
        :param name: name of unicorn
        :param hunger: hunger level of each unicorn
        :type name: str
        :type hunger: int
        """
        Animal.__init__(self, name, hunger)
        self._color = "Green"

    def talk(self):
        """print to screen dragon's talking option from Animal.talk()
        :return None but print to screen
        """
        super().talk()
        print(self.talk[4])

    def breath_fire(self):
        """ Special power of each dragon has
        :return None but print to program
        """
        print("$@#$#@$")


def main():
    """:main function running the zoo
    notes: #line:until line - subquestion
    """
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Sknuk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    zoo_lst = [brownie, zelda, stinky, keith, lizzy]    # 184:188 - 2.5.4
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_Jr = Sknuk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)
    zoo_lst.extend([doggo,kitty, stinky_Jr, clair, mcfly])    # 190:195 - 2.5.8
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()       # 196:199 - 2.5.4
        animal.talk()       #2.5.5
        if isinstance(animal,Dog): animal.fetch_stick()
        if isinstance(animal,Cat): animal.chase_laser()
        if isinstance(animal,Sknuk): animal.stink()
        if isinstance(animal,Unicorn): animal.sing()
        if isinstance(animal,Dragon): animal.breath_fire()      # 202:206 - 2.5.6
    print(Animal.zoo_name)      #2.5.9

if __name__ == "__main__":
    main()