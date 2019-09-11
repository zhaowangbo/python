from db import db_handler
from lib import common

bank_logger = common.get_logger("bank")


def check_balance_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        return user_dic["balance"]


def transfer_interface(to_name, transfer_balance, name):
    if to_name == name:
        return False, "you can not transfer to your self"

    else:
        to_user_dic = db_handler.select(to_name)
        user_dic = db_handler.select(name)
        if to_user_dic:
            if user_dic["balance"] >= transfer_balance:
                user_dic["balance"] -= transfer_balance
                to_user_dic["balance"] += transfer_balance

                user_dic["bankflow"].append("you transfer {} to {}".format(transfer_balance, to_name))
                to_user_dic["bankflow"].append("you receive {} from {}".format(transfer_balance, name))

                db_handler.save(user_dic)
                db_handler.save(to_user_dic)

                bank_logger.info("you receive {}$ from {}".format(transfer_balance, name))

                return True, "transfer successfully"
            else:
                return False, "you balance is not enough"

        else:
            return False, "the user does not exist"


def repay_interface(repay_balance, name):
    user_dic = db_handler.select(name)

    user_dic["balance"] += repay_balance
    user_dic["bankflow"].append("you have repayed {}".format(repay_balance))
    db_handler.save(user_dic)
    bank_logger.info("you repay {}".format(repay_balance))

    return True, "repay successfully"


def withdraw_interface(balance, name):
    user_dic = db_handler.select(name)
    balancel = balance * 1.05

    if user_dic["balance"] >= balancel:

        user_dic["balance"] -= balancel
        user_dic["bankflow"].append("you have withdraw {}".format(balance))

        db_handler.save(user_dic)
        bank_logger.info("you have withdraw {}".format(balance))

        return True, "you withdraw money successfully"

    else:
        return False, "your money is not enough"


def check_record_interface(name):
    user_dic = db_handler.select(name)
    for i in user_dic["bankflow"]:
        print(i)


def consume_interface(name, cost):

    user_dic = db_handler.select(name)
    if cost <= user_dic["balance"]:
        return True, "consume successfully"
    else:
        return False, "your money is not enough"