import time
import os


# def auth(func):
#     def wrapper(*args, **kwargs):
#         user_list = []
#         with open('user.txt') as file:
#             for line in file.readlines():
#                 user_list.append(line)
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
# # index = auth(index)
# @auth
# def index(name):
#     time.sleep(3)
#     print("welcome %s" % name)
#     return 1
# @auth
# def home(name):
#     time.sleep(3)
#     print("welcome %s" % name)
#     return 2
#
# index('albert')
# home('albert')
# db = 'user.txt'
# login_status = {"status": False}
#
# def auth(auth_type='file'):
#     def auth2(func):
#         def wrapper(*args, **kwargs):
#             if login_status["status"]:
#                 return func(*args, **kwargs)
#
#             if auth_type == 'file':
#                 with open(db, encoding='utf-8') as f:
#                     dic = eval(f.read())
#                     name = input("input you name").strip()
#                     pwd = input("input you pwd").strip()
#
#                     if name == dic["name"] and pwd == dic["password"]:
#                         login_status["status"] = True
#                         res = func(*args, **kwargs)
#                         return res
#                     else:
#                         print("wrong")
#             elif auth_type == 'sql':
#                 pass
#             else:
#                 pass
#         return wrapper
#     return auth2
#
#
#
# @auth()
# def index():
#     print("index")
# index()
#
# @auth("file")
# def home(name):
#     print(name)
#
# home("abc")

user = 'user.txt'
login_status = {"status": False}

def auth(file):
    def auth2(func):
        def wrapper(*args, **kwargs):

            if login_status["status"]:
                res = func(*args, **kwargs)
                return res

            else:
                with open(file, 'r') as f:
                    user = eval(f.read())

                name = input("input your name")
                password = input("in put your pwd")
                if name == user["name"] and password == user["password"]:
                    print("log successfully")
                    res = func(*args, **kwargs)
                    login_status["status"] = True
                    return res
        return wrapper
    return auth2

# auth(user) = auth2
# index = auth2(index)
@auth(user)
def index():
    print("welcom")

index()
index()