# class SingletonType(type):
#
#     def __init__(cls, *args, **kwargs):
#         cls.__instance = None
#         super().__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__call__(*args, **kwargs)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#
# class Spam(metaclass=SingletonType):
#     def __init__(self):
#         print("creating")
#
# # a = Spam()
# # print(a)
# b = Spam()
# print(b)

# class Singleton(object):
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls, *args, **kwargs)
#         return cls.__instance
#
# class Foo(Singleton):
#     a = 1

def create_singleton(cls):
    __instance = {}

    def inner():
        if cls not in __instance:
            __instance[cls] = cls()
        return __instance[cls]

    return inner

@create_singleton
class Singleton(object):
    def __init__(self):
        pass

st1 = Singleton()
st2 = Singleton()
print(st1)
print(st2)
