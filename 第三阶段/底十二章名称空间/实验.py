
class DeepShareStudent:
    school = 'deepshare'
    name = 'a'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def learn(self):
        print("%s is learning" % self)

    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")

stu1 = DeepShareStudent("王小二", 18, 'male')
stu2 = DeepShareStudent("王小三", 18, 'male')


# print(stu1)
# print(type(stu1))
# print(id(stu1))
#
# print(DeepShareStudent.__dict__)
print(id(DeepShareStudent.__dict__))
print(id(stu1.__dict__))
print(id(stu2.__dict__))

# print(DeepShareStudent.learn)
# print(stu1.learn)
# print(stu2.learn)
# print(id(DeepShareStudent.school))
# print(id(stu1.school))
# print(id(stu2.school))

# l1 = [1, 2, 3, 4]
# l2 = [0, 2, 3, 4]
# list.append(l1, 5)
# print(l1)

# class Bar:
#     n = 111
#
#     def __init__(self, x):
#         self.x = x
#
# obj = Bar("abc")
# obj.abc= 'a'
# print(obj.abc)
# del obj.abc
# print(obj.abc)

class Foo:
    count = 0

    def __init__(self):
        Foo.count+=1

obj1 = Foo()
obj2 = Foo()
print(obj2.count)

# class People:
#     def __init__(self, name, aggressivity, life_value=100):
#         self.name = name
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
#     def bite(self, enemy):
#         enemy.life_value -= self.aggressivity
#         print(enemy.life_value)
#
# class Dog:
#     def __init__(self, name, dog_type, aggressivity, life_value=100):
#         self.name = name
#         self.dog_type = dog_type
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
#     def bite(self, enemy):
#         enemy.life_value -= self.aggressivity
#         print(enemy.life_value)
#
# stu1 = Dog("abc",'asdf', 20)
# Dog.__init__(stu2, "abc",'asdf', 20)
# print(stu2)