import time
import os


def auth(func):
    def wrapper(*args, **kwargs):
        user_list = []
        with open('user.txt') as file:
            for line in file.readlines():
                user_list.append(line)

        if len(user_list) == 1:
            print("have never loged in")
            current_user = eval(user_list[0])

            name = input("input your username")
            password = input("input your password")

            if name == current_user['name'] and password == current_user['password']:
                print("successfully")

                with open('user.txt', 'r+') as file:
                    file.seek(0, 2)
                    file.write("True")
                return func(*args, **kwargs)

            else:
                print("username or password is wrong")

        else:
            print("you have loged in , you don't need to log in again!!")

            return func(*args, **kwargs)

    return wrapper

# index = auth(index)
@auth
def index(name):
    time.sleep(3)
    print("welcome %s" % name)
    return 1
@auth
def home(name):
    time.sleep(3)
    print("welcome %s" % name)
    return 2

index('albert')
home('albert')