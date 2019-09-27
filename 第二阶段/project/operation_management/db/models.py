
from db import db_handler


class BaseClass:

    def save(self):
        db_handler.save(self)

    @classmethod
    def get_obj_by_name(cls, name):
        obj = db_handler.select(name, cls.__name__.lower())
        return obj


class Admin(BaseClass):

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, school_name, address):
        School(school_name, address)

    def create_teacher(self, name, password):
        Teacher(name, password)

    def create_course(self, course_name):
        Course(course_name)


class Teacher(BaseClass):

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()




class Student(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school = None
        self.course_list = []
        self.scores = {}
        self.save()

    def get_school(self):
        return self.school

    def choose_school(self, name):
        self.school = name
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.scores[course_name] = 0
        self.save()


class School(BaseClass):

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.save()



class Course(BaseClass):
    def __init__(self, name):
        self.name = name
        self.student_list = []
        self.save()





