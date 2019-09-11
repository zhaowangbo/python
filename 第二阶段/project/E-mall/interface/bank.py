from db import db_handler
from lib import common

bank_logger = common.get_logger("bank")


def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic["balance"]


def transfer_interface(from_name, to_name, balance):
    if from_name == to_name:
        return False, "can not tranfer to your self"

    to_dic = db_handler.select(to_name)
    if to_dic:
        from_dic = db_handler.select(from_name)

        if from_dic["balance"] >= balance:
            to_dic["balance"] += balance
            from_dic["bankflow"].append("you transfer {}$ to {}".format(balance, to_name))
            to_dic["bankflow"].append("you receive {}$ from {}".format(balance, from_name))

            db_handler.save(from_dic)
            db_handler.save(to_dic)

            bank_logger.info("you receive {}$ from {}".format(balance, from_name))

            return True, "transfer successfully"

        else:
            return False, "your balance is not enouth"

    else:
        return False, "the to_name do not exist"


def repay_interface(name, balance):
    user_dic = db_handler.select(name)
    user_dic["balance"] += balance
    user_dic["bankflow"].append("repay %s $" % balance)
    db_handler.save(user_dic)
    bank_logger.info("you have repayed %s $" % balance)
    return True, "repay successfully"


def withdraw_interface(name, balance):
    user_dic = db_handler.select(name)
    balancel = balance * 1.05
    if user_dic["balance"] >= balancel:
        user_dic["balance"] -= balancel
        user_dic["bankflow"].append("you withdraw %s $" % balance)
        db_handler.save(user_dic)
        return True, "withdraw money successfully"

    else:
        return False, "balance is not enouth"


def check_record_interface(name):
    user_dic = db_handler.select(name)
    return user_dic["bankflow"]


def consume_interface(name, cost):
    user_dic = db_handler.select(name)
    if user_dic["balance"] >= cost:
        user_dic["balance"] -= cost
        db_handler.save(user_dic)
        return True, "consume sussfully"
    else:
        return False, "money is not enouth"
