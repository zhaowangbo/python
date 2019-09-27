# class ParentClass1:
#     pass
#
# class ParentClass2:
#     pass
#
# class SubClass1(ParentClass1):
#     pass
#
# class SubClass2(ParentClass1, ParentClass2):
#     pass


# class DeepsharePeople:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def info(self):
#         print(self.name, self.age, self.gender)


# class DeepshareTeacher(DeepsharePeople):
#
#     def __init__(self, name, age, gender, level, salary):
#         super().__init__(name, age, gender)
#         self.level = level
#         self.salary = salary
#
#     def modify_score(self):
#         print("teacher %s is modifying score" % self.name)
#
#     def info(self):
#         super().info()
#         print(self.level, self.salary)
#
# class DeepshareStudent(DeepsharePeople):
#
#     def choose(self):
#         print("student %s is choosing course" % self.name)

# tea1 = DeepshareTeacher('albert', 18, 'male', '10', '3.1')
# tea1.info()
# stu1 = DeepshareTeacher('张二哥偶', 18, 'female')

# print(tea1.__dict__)
# print(tea1.name)
#
# print(DeepshareStudent.__dict__)
# print(DeepsharePeople.__dict__)
#
# print(tea1.school)
# print(object)
# class Foo:
#     pass
# print(Foo.__bases__)

class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_birth(self):
        print("出生年月日%s%s%s" % (self.year, self.mon, self.day))

class DeepsharePeople:
    school = 'deepshare'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class DeepshareTeacher(DeepsharePeople):

    def __init__(self, name, age, gender, level, salary):
        super().__init__(name, age, gender)
        self.level = level
        self.salary = salary

    def modify_score(self):
        print("teacher %s is modifying score" % self.name)

class DeepshareStudent(DeepsharePeople):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def choose(self):
        print("student %s is choosing course" % self.name)

# teal = DeepshareTeacher('albert', 19, 'male', 10, 3.1)
# date_obj = Date(1996, 11, 20)
# date_obj.tell_birth()
# teal.birth = date_obj
# print(teal.birth)
# teal.birth.tell_birth()
# teal.modify_score()
#
# stu1 = DeepshareStudent("asd",16, "male", "ai")
# stu1.birth = Date(1992, 23, 3)
# stu1.birth.tell_birth()
#
# class Foo:
#     __x = 111
#
#     def __init__(self, y):
#         self.__y = y
#
#     def f1(self):
#         print("foo.f1")
# # obj = Foo(22)
# # print(Foo.__dict__)
# # print(obj.__dict__)
# # print(obj._Foo__x)
# obj.__aaaa = 1
# print(obj.__dict__)
# class Foo:
#     def __f1(self):
#         print("foo.f1")
#
#     def __f2(self):
#         print("foo.f2")
#         self.f1()
# class Bar(Foo):
#     def __f1(self):
#         print("bar.f1")
#
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height * self.height)
#
# albert = People("albert", 66, 1.80)
# albert.weight = 70
# print(albert.bmi)

# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         print("访问".center(50, '='))
#         return self.__name
#
#     @name.setter
#     def name(self, x):
#         print("修改".center(50, '='))
#         self.__name = x
#
#     @name.deleter
#     def name(self):
#         print("删除".center(50, '='))
#
#         del self.__name
#
# P = People('albert')
#
# P.name = 'Albert'
# del P.name

import setting
import time
import hashlib

# class People:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def tell(self):
#         print("%s %s" % (self.name, self.age))
#
#     @classmethod
#     def read_from_conf(cls):
#         return People(setting.NAME, setting.AGE)
#
#     @staticmethod
#     def create_id():
#         m = hashlib.md5()
#         m.update(str(time.clock()).encode('utf-8'))
#         return m.hexdigest()
#
# p = People(setting.NAME, setting.AGE)
# print(People.create_id)
# print(p.create_id)
# import abc
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractclassmethod
#     def talk(self):
#         pass
#
#     @abc.abstractclassmethod
#     def run(self):
#         pass
#
#     def abc(self):
#         print("b")
#
#
# class People(Animal):
#
#     def run(self):
#         print("a")
#
#     def talk(self):
#         print("a")
#
# a = People()
#
# a.abc()
    # def run(self):
    #     print("running")

# a = People()

import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print("say hello")

class Dog(Animal):




    def talk(self):
        print("heng")

def func(obj):
    obj.talk()

#
# p = People()
# d = Dog()
#
# func(p)
# func(d)
#


class Txt:
    def read(self):
        print("txt read")
    def write(self):
        pritn("txt write")


class Disk:
    def read(self):
        print("txta read")

    def write(self):
        pritn("txta write")

obj1 = Txt()
obj2 = Disk()
obj1.read()
obj2.read()