from interface import teacher_interface
from interface import common_interface
from lib import common

teacher_info = {
    "name": None
}


def out_login():
    if teacher_info["name"]:
        teacher_info["name"] = None
        print("out login successfully")
    else:
        print("you have never log in")



def teacher_login():
    while True:
        username = input("please input your username").strip()
        password = input("please input you password").strip()
        flag, msg = common_interface.common_login_interface(username, password, "teacher")
        if flag:
            print(msg)
            teacher_info["name"] = username
            break
        else:
            print(msg)


@common.login_auth(user_type="teacher")
def choice_course():
    print("choose the course you teach")
    while True:
        course_list = teacher_interface.get_all_course()


def check_course():
    pass


def check_student():
    pass


def modify_score():
    pass





func_dict = {
    "1": teacher_login,
    "2": choice_course,
    "3": check_course,
    "4": check_student,
    "5": modify_score,
    "6": logout
}


def teacher_view():
    while True:
        print("""
        1.login
        2.choice_course
        3.check_course
        4.check_student
        5.modify_score
        6.logout
        """)
        choice = input("please input choice function").strip()
        if choice not in func_dict:
            print("you should input number from 1 to 6")
            continue
        func_dict[choice]()






