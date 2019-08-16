# 写函数，检查字典的每一个value的长度,如果大于2，那么仅保
# # 留前两个长度的内容，并将新内容返回给调用者
def processing_dict(input):
    output= {}
    for key in input:
        if len(input[key]) > 2:
            output[key] = input[key][:2]
        else:
            output[key] = input[key]
    return output


a = {"a":"asdas", "b":[1, 2, 3, 4]}
b = processing_dict(a)
print(a)
print(b)
