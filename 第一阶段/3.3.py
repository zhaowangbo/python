def find_smaller_and_bigger(list_number, number):
    dict_number = {"k1": [], "k2": []}
    list_number = set(list_number)
    for i in list_number:
        if i > number:
            dict_number["k1"].append(i)
        elif i< number:
            dict_number["k2"].append(i)
    return dict_number


a = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90
b = find_smaller_and_bigger(a, 66)
print(b)
