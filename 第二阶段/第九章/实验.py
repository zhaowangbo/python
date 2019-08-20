# x = 12
# y = 11
#
# def max2(x, y):
#     return x if x > y else y
# print(max2(x, y))

# def get_age(n):
#     if n == 1:
#         return 18
#     return get_age(n-1) + 2
#
# print(get_age(5))

def tell(l):
    for item in l:
        if type(item) is not list:
            print(item)
        else:
            tell(item)

# items = [1, [2, [3, [4, [5, [6, [7, [8, [9, [10, ]]]]]]]]]]
# tell(items)

# f = lambda x, n: x ** n
# print(f)
#
# print(lambda x, n: x ** n)
# print(f(3, 4))

scalaries = {
    'james': 30000,
    'kd': 1000000,
    'zimuge': 100023,
    'harden': 9000023
}
def get(k):
    return scalaries[k]

# print(max(scalaries, key=get))
# print(max(scalaries, key=lambda x: scalaries[x]))
# print(min(scalaries, key=lambda x: scalaries[x]))
# print(sorted(scalaries, key=lambda x: scalaries[x]))
# print(sorted(scalaries, key=lambda x: scalaries[x], reverse=True))

nums = [1, 2, 3, 4]
res1 = map(lambda x: x ** 2, nums)

names = ['james', 'harden', 'curry']
res2 = map(lambda x: x + 'is a super star', names)


ages = [31, 19, 20, 22]
res3 = filter(lambda n: n > 30, ages)

res = '{1} {1} {1} '.format('albert', 18, 'male')

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "this gus is {self.name}, {self.age} years".format(self = self)


# print('{:.5f}'.format(3.1412432))
left = 'hello'
right = [1, 2, 3, 4]
right2 = {'x':1, "y":2, "z":3}
l1 = zip(left, right2) # [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]


# l = ["egg%s" % i for i in range(1, 10)
#                      for j in range(1,200)]
# print(l)
l = ("egg%s" % i for i in range(100))
# print(l)
# print(l.__next__())