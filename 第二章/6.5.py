# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应
# 的元素，并将其作为新列表返回给调用者。
def return_a_list(input):
    out_list = []

    for i in range(len(input)):
        if i % 2 != 0:
            out_list.append(input[i])
    return out_list


a = [1, 2, 3, 4, 5, 7, 7]
out = return_a_list(a)
print(out)
