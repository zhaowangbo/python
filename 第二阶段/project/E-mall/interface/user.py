from db import db_handler
from lib import common

user_logger = common.get_logger("user")


def login_interface(name, password):
    user_dict = db_handler.select(name)
    if user_dict:
        if password == user_dict["password"] and not user_dict["locked"]:
            return True, "login successfuly"
        else:
            return False, "password is wrong or the user is locked"
    else:
        return False, "the user doesn't exist"


def lock_user_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic["locked"] = True
        db_handler.save(user_dic)


def register_interface(name, password, balance=15000):
    user_dic = db_handler.select(name)

    if user_dic:
        return False, "the name have existed"

    else:
        user_dic = {
            "name": name,
            "password": password,
            "balance": balance,
            "credit": balance,
            "locked": False,
            "bankflow": [],
            "shoppingcart": []
        }
        db_handler.save(user_dic)
        user_logger.info("%s has registerd" % name)
        return True, "register successfuly"


