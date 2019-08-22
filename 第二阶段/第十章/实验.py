
import sys


# sys.path.append('C:\\Users\\赵望博\\Desktop\\python编程学习\\python\\第二阶段\\第十章\\a')
# print(sys.path)
#
#
# import time #优先导入内置模块， 重名无法导入自定义的模块
#
# from b import x1
# from spam import *
# print(money)
# change()

# import torch
# output = torch.rand(163200, 4)
# print(output.shape)
# a = output.reshape(1, -1, 4)
# print(a.shape)
#

# a, b = output.topk(2, dim=1, sorted=True)
# print(a)
# print(b)
# def foo(x, y, z, *args):
#     return 1
#     # print(x, y, z)
    # print(*args)
#     # print(args)
# foo(1, 2, 3, 4, 5, 6, 7)
# #
# # def foo(x, y, z, *args):
# #     print(x, y, z)
# #     print(args)
#
# foo(1, 2, 3, *[4, 5, 6, 7, 8])
# #
# def bar(x, y, z, **kargws):
#     print(x, y, z)
#     print(kargws)


# bar(1, 2, 3, **{'a': 1, 'b': 2})
#
# # def auth(name, pwd, **kwargs):
# #     print(name)
# #     print(pwd)
# #     print(kwargs)
#
# auth(name='Albert', pwd='123', group='group1')

# import time
#
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         print(stop_time - start_time)
#         return res
#
#     return wrapper
#
#
# def index():
#     print("index page")
#     return 1
#
#
# def home(a):
#     print(a)
#     return 2
# index = outer(index)
# print(index())
#
# hone = outer(home)
# home("sdfasdf")
#

import time

current_user = {
    'username': None
}


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("run time ", stop_time-start_time)
        return res

    return wrapper

def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print("have loged in")
            res = func(*args, **kwargs)
            return res

        name = input("input your name").strip()
        pwd = input("input your pwd").strip()

        if name =='albert' and pwd == '123':
            print("successfully")
            current_user['username'] = name
            res = func(*args, **kwargs)
            return res
        else:
            print("wrong")

    return wrapper






db = 'a.txt'
login_status = {'status': False}


def auth(auth_type='file'):
    def auth2(func):
        def wrapper(*args, **kwargs):
            if login_status['status']:
                return func(*args, **kwargs)
            if auth_type == 'file':
                with open(db, encoding='utf-8') as f:
                    dic = eval(f.read())
                name = input('username: ').strip()
                password = input('password: ').strip()
                if name == dic['name'] and password == dic['password']:
                    login_status['status'] = True
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                pass
            else:
                pass

        return wrapper

    return auth2


@auth()
def index():
    print('index')


@auth(auth_type='file')
def home(name):
    print('welcome %s to home' % name)


index()
home('albert')