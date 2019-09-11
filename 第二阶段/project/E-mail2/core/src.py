from interface import user
from interface import bank
from interface import shopping
from lib import common
user_data = {"name": None}


def login():

    print("login")
    if user_data["name"]:
        print("you have logined in")
        return

    count = 0
    while True:
        name = input("please input your name").strip()

        if name == 'q':
            break
        password = input("please input your password").strip()

        flg, msg = user.login_interface(name, password)

        if flg:
            user_data["name"] = name
            print(msg)
            break
        elif not flg and msg == "the name does not exist":
            print(msg)
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
        print("you have login")
        return

    while True:
        user_name = input("please input the user_name").strip()

        password = input("please input the password").strip()
        password_again = input("please input the password again").strip()

        if password == password_again:
            flg, msg = user.register_interface(user_name, password)

            if flg:
                print(msg)
                break
            else:
                print(msg)

        else:
            print("the two password is not same")


@common.login_auth
def check_balance():
    print("check the balance")
    balance = bank.check_balance_interface(user_data["name"])
    print(balance)


@common.login_auth
def transfer():
    print("transfer")
    while True:
        to_name = input("please input the user you want to transfer").strip()
        transfer_balance = input("please input the balance you want to transfer").strip()
        if transfer_balance.isdigit():
            transfer_balance = int(transfer_balance)
            flg, msg = bank.transfer_interface(to_name, transfer_balance, user_data["name"])

            if flg:
                print(msg)
                break
            else:
                print(msg)

        else:
            print("you must input digit")


@common.login_auth
def repay():
    print("repay")
    repay_balance = input("please input the money you want to repay").strip()
    if repay_balance.isdigit():
        repay_balance = int(repay_balance)
        flg, msg = bank.repay_interface(repay_balance, user_data["name"])

        if flg:
            print(msg)

    else:
        print("you must input number")


@common.login_auth
def withdraw():
    print("withdraw")
    balance = input("please input the money you want to withdraw").strip()
    if balance.isdigit():
        flg, msg = bank.withdraw_interface(balance, user_data["name"])
        if flg:
            print(msg)
        else:
            print(msg)
    else:
        print("you must input number")


@common.login_auth
def check_record():
    print("check record")
    flg, msg = bank.check_record_interface(user_data["name"])


@common.login_auth
def shop():

    print("shopping")

    goods = [["coffee", 20],
             ["chicken", 20],
             ["iphone", 8000],
             ["macpro", 15000],
             ["car", 100000]]

    for i, good in enumerate(goods):
        print(i, good[0] + ":" + str(good[1]) + "$")\


    shopping_cart = {}
    user_balance = bank.check_balance_interface(user_data["name"])
    cost = 0

    while True:
        choice = input("please input the number you want to buy").strip()
        if choice.isdigit():
            choice = int(choice)

            good_name = goods[choice][0]
            good_price = goods[choice][1]

            if user_balance >= good_price:

                if good_name not in shopping_cart:
                    shopping_cart.update({good_name: {"price": good_price, "count": 1}})

                else:
                    shopping_cart[good_name]["count"] += 1
                user_balance -= good_price
                cost += good_price

            else:
                print("money is not enouth")

        elif choice == 'q':
            if cost == 0:
                break
            print(shopping_cart)

            buy = input("do you want to buy y/n").strip()

            if buy == 'y':
                flg, msg = shopping.shopping_interface(user_data["name"], cost, shopping_cart)

                if flg:
                    print(msg)
                    break

                else:
                    print(msg)
                    break

            else:
                print("you dont buy anything")
                break
        else:
            print("illegality input")


@common.login_auth
def check_shopping_cart():
    print("check shopping cart")
    shopping_cart = shopping.check_shoppingcart_interface(user_data["name"])
    print(shopping_cart)







def logout():
    if user_data["name"]:
        user_data["name"] = None
        print("you have logout")
    else:
        print("you have never login")


user_operations = {
    "1": login,
    "2": register,
    "3": check_balance,
    "4": transfer,
    "5": repay,
    "6": withdraw,
    "7": check_record,
    "8": shop,
    "9": check_shopping_cart,
    "10": logout
}


def run():
    while True:

        print("""
        1:login,
        2:register,
        3:check_balance,
        4:transfer,
        5:repay,
        6:withdraw,
        7:check_record,
        8:shopping,
        9:check_shopping_cart,
        10:logout
        """)
        choice = input("please input the number from 1 to 10 to choice,and input 'q' to quit").strip()

        if choice == 'q':
            print("you have quited")
            break

        else:
            if choice.isdigit():
                operation = user_operations[choice]
                operation()
            else:
                print("you should input the number for 1 to 10")

    return 0






