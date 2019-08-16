def print_sym(sym, count):
    print(sym * count)

def print_msg(msg):
    print('\033[045m%s\033[0m' % msg)

def func():
    pass

def func1():
    return

def func2():
    return None

def func3():
    return 1


def func4():
    return 1, 2, [1, 2, 3]


def register(name, hobby, l=None):
    if l is None:
        l = []
    l.append(hobby)
    print(name, l)

def foo(x, y , z, *args):
    print(x, y, z)
    print(args)

def foo2(x, y, z, **kwargs):
    print(x, y, z)
    print(kwargs)


# foo(1, 2, 3, *[4, 5, 6, 7, 8])
# foo(1, 2, 3, *(4, 5, 6, 7, 8))

def bar(x, y, z, **kwargs):
    print(x, y, z)
    print(kwargs)

def sum2(*args):
    res = 0
    for num in args:
        res += num
    return res

def auth(name, pwd, **kwargs):
    print(name)
    print(pwd)
    print(kwargs)

def index(name, age, gender):
    print('welcome %s %s %s' % (name, age, gender))

def wrapper(*args,  **kwargs):
    print(args)
    index(*args, **kwargs)


def auth(*args, **kwargs):
    """    使用方式auth(name="Albert",pwd="123")
    :param args:
    :param kwargs:
    :return:
    """

    if len(args) != 0:
        print("shiyongguanjianzi")

    if 'name' not in kwargs:
        print("shiyong keyming name")
    if 'pwd' not in kwargs:
        print("a")

    name = kwargs['name']
    pwd = kwargs['pwd']
    print(name, pwd)

def foo3(*, x, y, z):
    print(x, y, z)

def auth2(*args, name, pwd):
    print(name, pwd)

auth2(1, 2, 3, name=1, pwd=2)

def foo4(x, y=1, *, z, m=2, **kwargs):
    print(x, y ,z, m)
    pass




# m=2是关键字参数的默认值    pass
