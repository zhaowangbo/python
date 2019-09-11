from db import db_handler
from lib import common
from interface import bank


def shopping_interface(name, cost, shoppingcart):
    user_dic = db_handler.select(name)

    flg, msg = bank.consume_interface(name, cost)

    if flg:
        print(msg)
        user_dic["shoppingcart"] = shoppingcart
        db_handler.save(user_dic)

        return True, "shop successfully"

    else:
        return False, msg


def check_shoppingcart_interface(name):
    user_dic = db_handler.select(name)
    return user_dic["shoppingcart"]

