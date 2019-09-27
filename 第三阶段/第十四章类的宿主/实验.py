#

# class Chinese:
#      country = "China"
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self):
#         print("%s speak chinese" % self.name)

# p = Chinese("albert", 18, "male")
# print(type(p))
# print(type(Chinese))
#
# def abc():
#     pass
#
#
# a = 54
# print()

class_name = "Chinese"
class_bases = (object, )
class_body = """
country = "China"

def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def speak(self):
    print("%s speak chinese" % self.name)
"""
# class_dic = {}
# exec(class_body, {}, class_dic)
# # print(class_dic)
#
# Chinese = type(class_name, class_bases, class_dic)
# print(Chinese)
# albert = Chinese("albert", 18, "male")
# print(albert.name)
#
# class MyType(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         if not class_name.istitle():
#             raise TypeError("daxie")
#         if not class_dic.get("__doc__"):
#             raise TypeError("wendang")
#         super(MyType, self).__init__(class_name, class_bases, class_dic)
#
#     def __call__(self, *args, **kwargs):
#         obj = object.__new__(self) #产生一个Foo类空对象
#
#         self.__init__(obj, *args, **kwargs)
#         print(*args)
#         # print(**kwargs)
#         return obj
# #Foo = MyType("Foo", (object, ), class_dic)
# class Foo(metaclass=MyType):
#     """
#     fasdf
#     """
#     def __init__(self, y, z):
#         self.y = y
#         self.z = z
#
#
#
# obj = Foo(213, 23)
# print(obj)

import setting
class MySQL:
    __instance = None
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def read_from_conf(cls):
        if not cls.__instance:
            obj = cls(setting.IP, setting.PORT)
            cls.__instance = obj

        return cls.__instance

obj1 = MySQL.read_from_conf()
obj2 = MySQL.read_from_conf()
obj3 = MySQL.read_from_conf()

print(obj1)
print(obj2)