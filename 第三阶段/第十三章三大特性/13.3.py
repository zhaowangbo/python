import abc


class Master:
    def __init__(self, name, pet):
        self.__name = name
        self.__pet = pet

    def feed(self):
        print("%s has prepared food" % self.__name)
        print("[%s]%s eat" % (self.__pet.type, self.__pet.name))
        self.__pet.eat()


class Pet(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.__name = name

    @abc.abstractmethod
    def eat(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


class Cat(Pet):
    def __init__(self, name, cat_type):
        super().__init__(name)
        self.__type = cat_type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def eat(self):
        print("cat eat")


class Dog(Pet):
    def __init__(self, name, dog_type):
        super().__init__(name)
        self.__type = dog_type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def eat(self):
        print("dog eat")


class Pig(Pet):
    def __init__(self, name, pig_type):
        super().__init__(name)
        self.__type = pig_type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def eat(self):
        print("pig eat")


cat1 = Cat("大橘子", "加菲猫")
m1 = Master("嫦娥", cat1)

m1.feed()
cat1.type = "a"
m1.feed()