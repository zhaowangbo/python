from interface import user
from interface import bank
from interface import shopping
from lib import common

user_data = {
    "name": None
}

def login():
    print("login")
    if user_data["name"]:
        print("have logied in")
        return 0
    else:
        count = 0
        while True:
            name = input("please input your name").strip()

            if name== 'q':
                break

            password = input("please input your password").strip()
            flag, msg = user.login_interface(name, password)
            if flag:
                user_data["name"] = name
                print(msg)
                break
            else:
                print(msg)
                count += 1
                if count == 3:
                    user.lock_user_interface(name)
                    print("the user has been locked")
                    break


def register():
    print("register")
    if user_data["name"]:
        print("you have loged in")
        return

    while True:
        name = input("please input your name").strip()

        if name == 'q':
            break

        password = input("input your password").strip()
        conf_password = input("confim your password").strip()
        if password == conf_password:
            flg, msg = user.register_interface(name, password)
            if flg:
                print(msg)
                break
            else:
                print(msg)

        else:
            print("the passwords are not same")


@common.login_auth
def check_balance():
    print("check the balance")
    balance = bank.check_balance_interface(user_data["name"])
    print(balance)



@common.login_auth
def trainsfer():
    print("trainsfer")
    while True:
        to_name = input("please input the name").strip()
        balance = input("input the balance you want to trainsfer").strip()
        if balance.isdigit():
            balance = int(balance)
            flag, msg = bank.transfer_interface(user_data["name"], to_name, balance)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.login_auth
def repay():
    print("repay money")
    balance = input("please input the money you want to repay").strip()
    if balance.isdigit():
        balance = int(balance)
        flg, msg = bank.repay_interface(user_data["name"], balance)


@common.login_auth
def withdraw():
    print("withdraw money")
    balance = input("input the money you want to withdraw").strip()
    if balance.isdigit():
        balance = int(balance)
        flag, msg = bank.withdraw_interface(user_data["name"], balance)
        if flag:
            print(msg)
        else:
            print(msg)
    else:
        print("you should input digit")


@common.login_auth
def check_record():
    print("check the record")
    bankflow = bank.check_record_interface(user_data["name"])
    for flow in bankflow:
        print(flow)

@common.login_auth
def shop():
    '''
    1 先循环打印出商品
    2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
    3 取出商品名，商品价格
    4 判断用户余额是否大于商品价格
    5 余额大于商品价格时，判断此商品是否在购物车里
        5.1 在购物车里，个数加1
        5.1 不在购物车里，拼出字典放入（｛‘good’：｛‘price’：10，‘count’：1｝｝）
    6 用户余额减掉商品价格
    7 花费加上商品价格
    8 当输入 q时，购买商品
        8.1 消费为0 ，直接退出
        8.2 打印购物车
        8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
    :return:
    '''

    print("shop")
    good_list = [["coffee", 20],
                 ["chicken", 20],
                 ["iphone", 8000],
                 ["macPro", 15000],
                 ["car", 1000000]]

    shoppingcart = {}

    cost = 0
    user_balance = bank.check_balance_interface(user_data["name"])
    while True:
        for i, good in enumerate(good_list):
            print("%s: %s" % (i, good))
        choice = input("please input the number of the good you want to buy").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice >= len(good_list):
                continue
            good_name = good_list[choice][0]
            good_price = good_list[choice][1]

            if user_balance >= good_price:
                if good_name in shoppingcart:
                    shoppingcart[good_name]["count"] += 1
                else:
                    shoppingcart[good_name] = {"price": good_price, "count": 1}
                user_balance -= good_price
                cost += good_price
            else:
                print("money is not enouth")
        elif choice == 'q':
            if cost == 0:
                break
            print(shoppingcart)
            buy = input("do you want to buy?y/n").strip()

            if buy == "y":
                flg, msg = shopping.shopping_interface(user_data["name"], cost, shoppingcart)

                if flg:
                    print(msg)
                    break
                else:
                    print(msg)


            else:
                print("you dont buy anything")
                break

        else:
            print("illegality input")


@common.login_auth
def check_shopping_cart():
    print("check shopping_cart")
    shoppingcart = shopping.check_shoppingcart(user_data["name"])
    print(shoppingcart)


def logout():
    user_data["name"] = None







func_dic = {
    "1": login,
    "2": register,
    "3": check_balance,
    "4": trainsfer,
    "5": repay,
    "6": withdraw,
    "7": check_record,
    "8": shop,
    "9": check_shopping_cart,
    "10": logout
}

def run():
    while True:
        print('''
        1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品
        10、退出登陆
        ''')
        choice = input("pleasce choice").strip()
        if choice in func_dic:
            func_dic[choice]()
        else:
            print("please input number from 1 to 10")