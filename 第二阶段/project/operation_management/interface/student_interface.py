from db import models
from lib import common

logger = common.get_logger("student")


def student_register_interface(name, password):
    student_obj = models.Student.get_obj_by_name(name)
    if student_obj:
        return False, "the student has existed"
    else:
        models.Student(name, password)
        return True, "register successfully"


def choose_school_interface(student_name, school_name):
    student_obj = models.Student.get_obj_by_name(student_name)
    school = student_obj.get_school()
    if not school:
        student_obj.choose_school(school_name)
        logger.info("%s has choose shcool %s" % (student_name, school_name))
        return True, "choose school successfully"
    else:
        return False, "you have choose school"


def get_can_choose_course_interface(name):
    obj = models.Student.get_obj_by_name(name)
    if not obj.school:
        return False, "you have never choose school"
    school_obj = models.School.get_obj_by_name(obj.school)
    if school_obj.course_list:
        return True, school_obj.course_list
    else:
        return False, "this school do not have course"


def choose_course_interface(student_name, course_name):
    obj = models.Student.get_obj_by_name(student_name)
    if course_name in obj.course_list:
        return False, "you have choose this course"
    obj.add_course(course_name)
    logger.info("%s choose %s" % (student_name, course_name))
    return True, "choose course successfully"


def check_score_interface(name):
    student_obj = models.Student.get_obj_by_name(name)
    return student_obj.scores
