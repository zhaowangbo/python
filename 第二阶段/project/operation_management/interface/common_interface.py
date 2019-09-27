import logging.config
from conf import settings
from db import models
from core import admin
from core import teacher
from core import student
import os


def common_login_interface(name, password, user_type):
    global obj

    if user_type == "admin":
        obj = models.Admin.get_obj_by_name(name)

    elif user_type == "teacher":
        obj = models.Teacher.get_obj_by_name(name)

    elif user_type == "student":
        obj = models.Student.get_obj_by_name(name)

    if obj:

        if obj.password == password:
            return True, "login successfully"
        else:
            return False, "password not right"

    else:
        return False, "user do not exist"


def get_all_dir_obj(path):
    if os.path.exists(path):
        obj_list = os.listdir(path)
        return obj_list
    else:
        return None


def check_all_schools():
    path = os.path.join(settings.BASE_DB, "school")
    return get_all_dir_obj(path)