# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个
# 长度的内容，并将新内容返回给调用者。
def processing_list(input_list):

    if len(input_list) > 2:
        target_list = input_list[:2]
    else:
        target_list = input_list

    return target_list

a = [1, 2, 3, 4, 5]
b = [1]

print(processing_list(a))
print(processing_list(b))