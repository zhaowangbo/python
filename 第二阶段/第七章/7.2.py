import time


loged_in = False

def timer(func):
    def wrapper(*args, **kwargs):
        start_stime = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        t = stop_time - start_stime
        return t
    return wrapper

def auth(func):
    def wrapper(*args, **kwargs):
        global loged_in
        if loged_in == False:
            with open('user.txt', 'r') as file:
                lines = file.readlines()
            with open("user.txt", 'w') as file:
                for line in lines:
                    if line == 'True':
                        continue
                    file.write(line)

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

                loged_in = True

                return func(*args, **kwargs)

            else:
                print("username or password is wrong")

        else:
            print("you have loged in , you don't need to log in again!!")

            return func(*args, **kwargs)

    return wrapper


# index = time(auth(index))
@timer
@auth
def index():
    time.sleep(1)
    print("welcome to inde page")
    time.sleep(3)
    return 1



t = index()

print(t)
if t > 10:
    loged_in=False

@timer
@auth
def home():
    time.sleep(1)
    print("welcome to inde page")
    return 2

home()