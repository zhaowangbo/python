from lib import common
from interface import student_interface
from interface import common_interface


student_info = {
    "name": None
}


def logout():
    if not student_info["name"]:
        print("you have never login")
    else:
        student_info["name"] = None


def student_login():
    while True:
        username = input("please input your username").strip()
        password = input("please input you password").strip()
        flag, msg = common_interface.common_login_interface(username, password, "student")
        if flag:
            print(msg)
            student_info["name"] = username
            break
        else:
            print(msg)


def student_register():
    while True:
        name = input("please input your name").strip()
        password = input("please input you password").strip()
        conf_password = input("please input you password again").strip()
        if password == conf_password:
            flg, msg = student_interface.student_register_interface(name, password)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("password are not same")


@common.login_auth(user_type="student")
def choose_school():
    print("choose school")
    school_list = common.check_all_schools()
    if not school_list:
        print("there is no school")
        return
    for i, school in enumerate(school_list):
        print("%s：%s" % (i, school))
    choice = input("please choose school")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(school_list):
            flg, msg = student_interface.choose_school_interface(student_info["name"], school_list[choice])
            print(msg)
        else:
            print("there is no this school")
    else:
        print("please input digit")


@common.login_auth(user_type="student")
def choose_course():
    print("choose course")
    flg, course_list = student_interface.get_can_choose_course_interface(student_info["name"])
    if not flg:
        print(course_list)
    for i, course in enumerate(course_list):
        print("%s：%s" % (i, course))
    choice = input("please input course")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(course_list):
            flg, msg = student_interface.choose_course_interface(student_info["name"], course_list[choice])
            print(msg)
        else:
            print("there is no this course")
    else:
        print("please input digit")



















@common.login_auth(user_type="student")
def check_score():
    scores = student_interface.check_score_interface(student_info["name"])
    print(scores)




func_dic = {
    "1": student_register,
    "2": student_login,
    "3": choose_school,
    "4": choose_course,
    "5": check_score,
    "6": logout
}


def student_view():
    while True:
        print('''
        1 注册
        2 登陆
        3 选择学校
        4 选择课程
        5 查看成绩
        6 退出登陆
        ''')
        choice = input("please input number to choice").strip()
        if choice == "q":
            break
        if choice not in func_dic:
            print("you must input number for 1 to 6")
            continue

        func_dic[choice]()