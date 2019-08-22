# import time
#
#
# loged_in = False
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_stime = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         t = stop_time - start_stime
#         return t
#     return wrapper
#
# def auth(func):
#     def wrapper(*args, **kwargs):
#         global loged_in
#         if loged_in == False:
#             with open('user.txt', 'r') as file:
#                 lines = file.readlines()
#             with open("user.txt", 'w') as file:
#                 for line in lines:
#                     if line == 'True':
#                         continue
#                     file.write(line)
#
#         user_list = []
#         with open('user.txt') as file:
#             for line in file.readlines():
#                 user_list.append(line)
#
#
#         if len(user_list) == 1:
#             print("have never loged in")
#             current_user = eval(user_list[0])
#
#             name = input("input your username")
#             password = input("input your password")
#
#             if name == current_user['name'] and password == current_user['password']:
#                 print("successfully")
#
#                 with open('user.txt', 'r+') as file:
#                     file.seek(0, 2)
#                     file.write("True")
#
#                 loged_in = True
#
#                 return func(*args, **kwargs)
#
#             else:
#                 print("username or password is wrong")
#
#         else:
#             print("you have loged in , you don't need to log in again!!")
#
#             return func(*args, **kwargs)
#
#     return wrapper
#
#
# # index = time(auth(index))
# @timer
# @auth
# def index():
#     time.sleep(1)
#     print("welcome to inde page")
#     time.sleep(3)
#     return 1
#
#
#
# t = index()
#
# print(t)
# if t > 10:
#     loged_in=False
#
# @timer
# @auth
# def home():
#     time.sleep(1)
#     print("welcome to inde page")
#     return 2
#
# home()

import time
import random
user_data = {
    'user':None,
    "login": False,
    "now_time": time.time()
}
db_username = 'albert'
db_password = '123'



def auth(func):
    def wrapper(*args, **kwargs):
        passed_time = time.time() - user_data["now_time"]

        if user_data["user"] and passed_time < 3:
            return func(*args, *kwargs)

        else:
            while True:
                username = input("input you username")
                pwd = input("input your pwd")

                if username == db_username and pwd == db_password:
                    print("log in successfully")
                    user_data["user"] = username
                    user_data["login"] = True
                    user_data["now_time"] = time.time()

                    return func(*args, **kwargs)
                else:
                    print("wrong")
    return wrapper

@auth
def index():
    print("this is index page")

@auth
def home(name):
    print("this is %s home page" % name)

index()
time.sleep(1)
home("zhao")
time.sleep(3)
home("zhao")