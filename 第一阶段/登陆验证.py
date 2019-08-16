def load(name, password):
    i = 0
    while i < 3:
        print("you only have {0:d} chances".format(3 - i))
        input_name = input("please enter your name")
        input_password = input("please enter your password")
        if input_name == name and int(input_password) == password:
            print("load successfully")
            i = 0
            if input("enter 'q' to quit") == 'q':
                break
        else:
            i += 1
            if i == 3:
                print("you have enter wrong threes times")
            else:
                print("name or password is not right, please try again")


right_name = "zhaowangbo"
right_password = 123456
load(right_name, right_password)

