# def func1():
#     print("from func1")
#
#     def func2():
#         print("from func2")
#     print(func2)
#     func2()


#
# def f1():
#     len =1
#
#     def f2():
#         len = 2
#         print(len)
#
#     len =3
#     f2()
#
#
# def make_counter():
#     count = 0
#
#     def check_counter():
#         print(count)
#
#     def modify_counter():
#         nonlocal count
#         count += 1
#         print(count)
#     modify_counter()
#
#
# def bar():
#     print("from bar")
# def foo(func):
#     return func
#
#
# def auth():
#     print("登陆")
# def register():
#     print("注册")
#
# func_dict = {'1': auth,
#              '2': register}
#
# def interactive():
#     while True:
#         print("1 ,2")
#
#         choice = input("1 or 2")
#
#         if choice in func_dict:
#             func_dict[choice]()
#
#
#
#
#
#
#
# import time
#
#
# def index():
#     time.sleep(1)
#     print("welcome to index page")
#     return 1
#
# def home(name):
#     time.sleep(2)
#     print("welcome %s to index page" % name)
#     return 2
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         end_time = time.time()
#         print("run time is %s" % (end_time - start_time))
#         return res
#
#     return wrapper
#
# index = timer(index)
# home = timer(home)
#
# home('albert')
# print(home())

import time
current_user = {
    'username': None
}

# def auth(func):
#     def wrapper(*args, **kwargs):
#         if current_user['username']:
#             print("已经登陆过了")
#             res = func(*args, **kwargs)
#             return res
#
#         name = input("用户名").strip()
#         pwd = input("密码").strip()
#         if name =='albert' and pwd == '1':
#             print("登陆成功")
#             current_user['username'] = name
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print("用户名密码错误")
#
#     return wrapper
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_stime = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         print(stop_time - start_stime)
#         return res
#     return wrapper
#
# # index = timer(auth(index))
# @timer
# @auth
# def index():
#     time.sleep(1)
#     print("welcome to inde page")
#     return 1

#
from functools import wraps
def auth(engine):
    def user_auth(func):
        # @wraps(func)  # 加在最内层函数正上方
        def wrapper(*args, **kwargs):
            if engine == 'file':
                print("基于文件的认证")
                if current_user['username']:
                    print("已经登陆过了")
                    res = func(*args, **kwargs)
                    return res

                name = input("用户名").strip()
                pwd = input("密码").strip()
                if name == 'albert' and pwd == '1':
                    print("登陆成功")
                    current_user['username'] = name
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("用户名密码错误")

            elif engine == 'engine':
                print("基于mysql的认证")
            elif engine == 'ldap':
                print("基于ldap的认证")
            elif engine == 'post':
                print("基于post的认证")
        return wrapper

    return user_auth

@auth("file")
def index():
    time.sleep(1)
    print("welcome to inde page")
    return 1



from functools import wraps
def deco(func):
    # @wraps(func)  # 加在最内层函数正上方
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@deco
def index():
    '''哈哈哈哈'''
    print(index.__doc__)

index()
