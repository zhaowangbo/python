# 列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，去重得到新列表,且新列表无需保持列表原来的顺序
# 在上题的基础上，保存列表原来的顺序
# 有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序

l = ["a", "b", "1", "a", "a"]

# 1
l1 = set(l)
print(l1)

# 2
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

# 3
l = [
    {"name": "albert", "age": 18, "sex": "male"},
    {"name": "james", "age": 35, "sex": "male"},
    {"name": "taylor", "age": 25, "sex": "female"},
    {"name": "albert", "age": 18, "sex": "male"},
    {"name": "albert", "age": 18, "sex": "male"},
    {"name": "albert", "age": 18, "sex": "male"},

]

l3 = []
for i in l:
    if i not in l3:
        l3.append(i)
print(l3)


