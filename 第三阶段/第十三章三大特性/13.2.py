class DeepsharePeople:
    school = "deepshare"

    def __init__(self, name, age, sex):
        self.name = name
        self.age =age
        self.sex = sex


class DeepshareTeacher(DeepsharePeople):

    def __init__(self, name, age, sex, level, salary):
        super(DeepshareTeacher, self).__init__(name, age, sex)
        self.level = level
        self.salary = salary

        self.courses = []

    def change_score(self):
        print("teacher is changing score")

    def tell_course_info(self):
        print("techer {} has coures:".format(self.name, self))
        for course in self.courses:
            course.info()


class DeepshareStudent(DeepsharePeople):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.courses = []

    def choose(self):
        print("student %s choose course" % self.name)

    def tell_course_infor(self):
        print("student {} has courese:".format(self.name))

        for course in self.courses:
            course.info()


class Course:

    def __init__(self, cname, period, price):
        self.cname = cname
        self.period = period
        self.price = price

    def info(self):
        print("name:{}, peiod:{}, price:{}".format(self.cname, self.period, self.price))


tea1 = DeepshareTeacher('Albert', 18, 'male', 9, 3.1)
stu1 = DeepshareStudent('张三', 16, 'male')

python = Course("python", "2mons", 2000)
database = Course("database", "3mons", 500)

tea1.courses.append(python)
stu1.courses.append(database)
stu1.tell_course_infor()