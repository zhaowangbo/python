# import time
#
# def timer(func):
#     def wrapper(path):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         with open(path, 'r+') as file:
#             file.seek(0, 2)
#             file.write(str(stop_time - start_time)+ '\n')
#
#     return wrapper
#
# # index = timer(index)
# @timer
# def index():
#     time.sleep(3)
#     print("welcome")
#
# index("log.txt")

import time

def add_log(file):
    def wrapper(func):
        def inner(*args, **kwargs):
            with open(file, 'a', encoding='utf-8') as f:
                f.write('[%s]:[%s]\n' % (func.__name__, time.strftime('%Y-%m-%d %X')))
                res = func(*args, **kwargs)
                return res
        return inner
    return wrapper


@add_log("db1.txt")
def index():
    print("this is index page")
    return 1

a = index()

@add_log("db2.txt")
def home(name):
    print("this is %s home" % name)
    return 2

b = home("zhao")