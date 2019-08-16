def question1():
    i = 1
    number = ''
    while i <= 10:

        if i == 7:
            number = number + "  "
        else:
            number = number + str(i) + " "

        i = i + 1

    print(number)


question1()


def question2():
    sum = 0
    for i in range(1, 101, 1):
        sum = sum + i

    print(sum)


question2()


def question3():
    sum = 0
    for i in range(1, 101, 1):
        if i % 2 != 0:
            sum = sum + i
    print(sum)


question3()


def question4():
    sum = 0
    for i in range(1, 101, 1):
        if i % 2 == 0:
            sum = sum + i
    print(sum)


question4()


def question5():
    sum = 0
    for i in range(1, 100, 1):
        if i % 2 != 0:
            sum = sum + i
        elif i % 2 == 0:
            sum = sum - i
    print(sum)


question5()