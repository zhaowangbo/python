from core import admin
from core import student
from core import teacher


func_dict = {
    "1": admin.admin_view,
    "2": teacher.teacher_view,
    "3": student.student_view
}


def run():
    while True:
        print("""
        1.admin
        2.teacher
        3.student
        """)
        choice = input("please choice your identity").strip()
        if choice not in func_dict:
            print("please input number from 1 to 3")
            continue

        func_dict[choice]()

