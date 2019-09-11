def get_data(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_data(n-1) + get_data(n-2)



for i in list(range(1000)):

    print(get_data(i+1))