
dict_user = {'Albert': "超级管理员", 'tom': "普通管理员", 'jack': "业务主管", 'rain': "业务主管"}
dict_user.update({"dfasdf": "dsfa"})
print(dict_user)

while True:
    name = input("enter your name and enter 'q' to quit")

    if name == 'q':
        break

    if not (name in dict_user):
        print("普通用户")
    else:
        print(dict_user[name])



