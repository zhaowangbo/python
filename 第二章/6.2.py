# 计算传入字符串中【数字】、【字母】、【空格] 以及
# 【其他】的个数

def processing_str(strs):
    number = 0
    aplhabet = 0
    space = 0
    others = 0
    for i in strs:
        if i.isdigit():
            number += 1

        elif i.isalpha():
            aplhabet += 1

        elif i == ' ':
            space += 1

        else:
            others+=1

    return number, aplhabet, space, others

a = "asdfa123(()(*&%%$12342sd"
number, aplhabet, space, others = processing_str(a)
print(number, aplhabet, space, others)
