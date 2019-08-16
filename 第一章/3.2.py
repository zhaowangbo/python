# 有列表data=['albert',18,[2000,1,1]]，
# 分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量

data = ["albert", 18, [2000, 1, 1]]
birthday = {"year": None, "month": None, "day": None}
name = 0
age = 0

for i in data:
    if isinstance(i, str):
        name = i
    elif isinstance(i, int):
        age = i
    else:
        birthday["year"], birthday["month"], birthday["day"] = i[0], i[1], i[2]

print(name)
print(age)
print(birthday)
