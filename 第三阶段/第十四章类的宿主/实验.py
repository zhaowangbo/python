# class Foo:
#     pass
#
# foo = Foo()
#
# print(isinstance("abc", str))
# print(issubclass(Foo, object))

# class People:
#     country = "china"
#
#     def __init__(self, name):
#         self.name = name
#
#     def tell(self):
#         print("%s is aaa" % self.name)
#
# obj = People("albert")
# print(People.__dict__)
# print(hasattr(People, "country"))
# print(hasattr(People, ""))
# x = getattr(People, "tell", None)
# print(x)
# # obj.tell()
# setattr(People, 'x', 111)
# print(People.x)
#
# delattr(People, "country")
# print(People.__dict__)

# class Foo:
#     def run(self):
#         while True:
#             cmd = input("cmd>> ").strip()
#             if hasattr(self, cmd):
#                 func = getattr(self, cmd)
#                 func()
#             elif cmd == 'exit':
#                 break
#
#     def download(self):
#         print("downloading")
#
#     def upload(self):
#         print("uploading")
# obj = Foo()
# obj.run()

# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return "name: %s, age: %s" % (self.name, self.age)
#
#     def __del__(self):
#         print("__del__")
#
# obj = People("albert", 18, "male")
#
# del obj
# print(obj)

class MyOpen:
    def __init__(self, file_path, mode='r', encoding="utf-8"):
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding
        self.file_obj = open(file_path, mode=mode, encoding=encoding)

    def __str__(self):
        msg = """        file_path:%s        
        mode:%s        
        encoding:%s        
        """ % (self.file_path, self.mode, self.encoding)

        return msg

    def __del__(self):
        print("del")
        self.file_obj.close()
#
# f = MyOpen("acb.txt", mode='r', encoding='utf-8')
#
# res = f.file_obj.read()
# del f
# f.file_obj
# class Foo:
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "123"
#
#     def __del__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print("__call__", args, kwargs)

# code = """
# x = 1
# y = 2
# def f1(self, a, b):
#     pass
# """
# global_dic = {'x':999}
# local_dic = {}
#
# exec(code, global_dic, local_dic)
# print(global_dic)
# print(local_dic)

# Chinese = type(..)
# class Chinese:
#     country = "China"
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self):
#         print("%s is speak chinese" % self.name)
# # print(Chinese.__dict__)
# p = Chinese("albert", 12, "male")
# print(type(p))
# print(type(Chinese))\

class_name ="Chinese"
class_bases=(object, )
class_body="""
country = "China"
def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def speak(self):
        print("%s is speak chinese" % self.name)
"""

# class_dic = {}
# exec(class_body, {}, class_dic)
# # print(class_dic)
# Chinese= type(class_name, class_bases, class_dic)
#
# albert = Chinese("albert", 18, "male")
# print(albert.name, albert.age, albert.gender)

class MyType(type):

    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError("类的名字必须大写")

        # if not class_dic.get("__doc__"):
        #     raise TypeError("类中必须写好注释文档")

        super(MyType, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        obj = object.__new__(self)

        self.__init__(obj, *args, **kwargs)

        return obj


class Foo(metaclass=MyType):
    def __init__(self, y):
        self.y = y

    def f1(self):
        print("from f1")

    pass


# \
# obj = Foo()
# print(obj)
# class Student:
#     """
#     fasdfsad
#     """
# print(Student.__doc__)
# print(Student.__dict__)

class MySQL:
    __instance = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def creat_singleton(cls):
        if not cls.__instance:
            obj = cls(123, 123123123)
            cls.__instance = obj
        return cls.__instance

# obj1 = MySQL.creat_singleton()
# obj2 = MySQL.creat_singleton()
# print(obj1)
# print(obj2)