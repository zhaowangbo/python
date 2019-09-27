import logging.config
from conf import settings
from db import models
import os


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    return logging.getLogger(name)


def login_auth(user_type):
    from core import admin, student, teacher

    def auth(func):
        def wrapper(*args, **kwargs):

            if user_type == 'admin':
                if not admin.admin_info["name"]:
                    admin.admin_login()
                else:
                    return func(*args, **kwargs)

            if user_type == 'teacher':
                if not teacher.teacher_info["name"]:
                    teacher.teacher_login()
                else:
                    return func(*args, **kwargs)

            if user_type == 'student':
                if not student.student_info["name"]:
                    student.student_login()
                else:
                    return func(*args, **kwargs)
        return wrapper

    return auth

def get_all_dir_obj(path):
    if os.path.exists(path):
        obj_list = os.listdir(path)
        return obj_list
    else:
        return None