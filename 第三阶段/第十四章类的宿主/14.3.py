class CarMeta(type):
    def __call__(self, *args, **kwargs):
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        print(dir(obj))

        if "production_date" in dir(obj) and \
            "engine_number" in dir(obj) and \
            "capacity" in dir(obj):

            return obj
        else:
            raise TypeError("asd")

class Car(metaclass=CarMeta):
    def __init__(self, name, production_date, engine_number, capacity):
        self.name = name
        self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity

car = Car('红旗HS7', '2019.9.3', 9527, 5)