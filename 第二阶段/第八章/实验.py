# str1 = 'hello' # 可迭代对象
# iter_str1 = str1.__iter__()  # 迭代器对象
# print(iter_str1.__next__())  # 取出迭代器对象的一个值
# print(iter_str1.__iter__() is iter_str1)  # 迭代器对象__iter__方法还是迭代器对象本身
# print(iter_str1.__iter__().__iter__().__iter__().__iter__() is iter_str1)


# f = open("a.txt", 'r', encoding='utf-8')
# print(f.__iter__() is f)
# print(f.__next__())

# set1 = {1, 2, 3, 4, 5}
# iter_set1 = set1.__iter__()
#
# while True:
#     try:
#         print(iter_set1.__next__())
#     except StopIteration:
#         break

# item = range(1000000000000000)
# iter_item = item.__iter__()
# while True:
#     print(iter_item.__next__())

# x = [1, 2, 3]
# iter_x = x.__iter__()
# print(len(iter_x))
# # while True:
#
#     try:
#         print(iter_x.__next__())
#     except StopIteration:
#         break

# iter_x.__next__()

def test_yield():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3
#
# res = test_yield()
# print(res)
# print(res.__iter__())
# print(res.__next__())
# print(res.__next__())

# print(range(10, 1))

# def show_my_range(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
# for item in show_my_range(1, 10, 3):
#     print(item)


def eat(name):
    print("&%s is ready for eating " % name)
    food_list = []
    while True:
        food = yield food_list
        print("%s starts to eat %s" % (name, food))
        food_list.append(food)



personal = eat('albert')

personal.__next__()
# or personal.send(None)
res1 = personal.send("abc")
print(res1)
res2 = personal.send("sadf")
print(res2)
# res2 = personal.send("sadddf")
