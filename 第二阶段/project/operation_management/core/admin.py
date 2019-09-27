from interface import admin_interface
from lib import common
from interface import common_interface

admin_info = {
    "name": None
}


def logout():
    if admin_info["name"]:
        admin_info["name"] = None
        print("log out successfully")
    else:
        print("you have never login")


def register():
    while True:
        username = input("please input your username").strip()
        password = input("please input password").strip()
        password_again = input("please input password again").strip()

        if password == password_again:
            flag, msg = admin_interface.admin_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("two input must be same")

    pass


def admin_login():
    while True:
        username = input("please input your username").strip()
        password = input("please input you password").strip()
        flag, msg = common_interface.common_login_interface(username, password, "admin")
        if flag:
            print(msg)
            admin_info["name"] = username
            break
        else:
            print(msg)


@common.login_auth("admin")
def create_school():
    while True:
        school_name = input("please input school name").strip()
        address = input("please input school address").strip()
        flag, msg = admin_interface.create_school_interface(admin_info["name"], school_name, address)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth("admin")
def create_teacher():
    while True:
        teacher_name = input("please input teacher name ").strip()
        flag, msg = admin_interface.create_teacher_interface(admin_info["name"], teacher_name)

        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth("admin")
def create_course():
    print("create course")
    while True:
        school_list = common.check_all_schools()
        if school_list:
            for i, school in enumerate(school_list):
                print("%s: %s" % (i, school))
            choice = input("please choose a shool").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(school_list):
                    print("there is not this school")
                    continue

                course_name = input("please input the name of the course").strip()
                flag, msg = admin_interface.create_course_interface(admin_info["name"], course_name, school_list[choice])

                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print("please input digit")
        else:
            print("there is no school")


func_dict = {
    "1": register,
    "2": admin_login,
    "3": create_school,
    "4": create_teacher,
    "5": create_course,
    "6": logout
}


def admin_view():
    while True:
        print("""
        1.register
        2.login
        3.create_school
        4.create_teacher
        5.create_course
        6.logout
        """)
        choice = input("please input choice function").strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print("you should input number from 1 to 6")
            continue
        func_dict[choice]()









