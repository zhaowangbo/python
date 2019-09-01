# str1 = "hello"
# print(str1.__iter__())
# print(str1.__iter__().__iter__())
#
# def test_yield():
#     print("a")
#     yield 1
#     print("b")
#     yield 2
#
# res = test_yield()
# print(res)
# print(res.__next__())
# x = 12
# y = 11
#
# res = x if x > y else y
# print(res)
#
# res = "{} {} {}".format('albert', "123", "213")
# nums = [1, 2, 3, 4]
# res = map(lambda x: x ** 2, nums)
ages = [18, 19, 10, 32, 99, 2]
res = filter(lambda n: n >=30, ages)
print(list(res))