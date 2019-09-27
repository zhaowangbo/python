from db import db_handler
from db import models
from lib import common


logger = common.get_logger("admin")


def admin_register_interface(name, password):
    admin_obj = models.Admin.get_obj_by_name(name)
    if admin_obj:
        return False, "admin has been registered"

    else:
        models.Admin(name, password)
        logger.info("admin register successfully")
        return True, "successfully"


def create_school_interface(admin_name, school_name, address):
    school_obj = models.School.get_obj_by_name(school_name)

    if school_obj:
        return False, "the school has existed"
    admin_obj = models.Admin.get_obj_by_name(admin_name)
    admin_obj.create_school(school_name, address)
    logger.info("admin %s create school successfully" % admin_name)

    return True, "create school successfully"


def create_teacher_interface(admin_name, name, password="465"):
    obj = models.Teacher.get_obj_by_name(name)
    if obj:
        return False, "teacher has existed"
    else:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_teacher(name, password)
        logger.info("admin %s has created teacher %s successfully" % (admin_name, name))
        return True, "create successfully"


def create_course_interface(admin_name, course_name, school_name):
    obj = models.Course.get_obj_by_name(course_name)
    if obj:
        return False, "the course has existed"

    else:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_course(course_name)
        logger.info("admin %s create course %s in school %s" % (admin_name, course_name, school_name))
        return True, "course has been created successfully"

