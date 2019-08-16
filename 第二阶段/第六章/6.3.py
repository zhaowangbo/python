# 写函数，判断用户传入的对象（字符串、列表、元组）长度是
# 否大于5
def judge_len(target):
    if len(target) > 5:
        return True
    else:
        return False

a = {"a":1, "as":2}
b = (1, 2, 3, 4, 5, 5)
print(judge_len(a))
