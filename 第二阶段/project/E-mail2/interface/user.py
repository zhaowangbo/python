from db import db_handler
from lib import common

user_logger = common.get_logger("user")




def login_interface(name, password):

    user_dic = db_handler.select(name)
    if user_dic:
        if password == user_dic["password"] and not user_dic["locked"]:
            return True, "you login successfully"
        else:
            return False, "the password is not right or locked"

    else:
        return False, "the name does not exist"


def lock_user_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic["locked"] = True
        db_handler.save(user_dic)















def register_interface(name, password, balance=15000):
    user_dic = db_handler.select(name)
    if user_dic:
        return False, "the name has existed"

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

    return True, "register successfully"






