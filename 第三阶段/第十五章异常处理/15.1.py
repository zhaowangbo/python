









class SlopOverError(BaseException):

    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self):
        return "<%s %s>" % (number, message)

    def verify_slop_over(self):
        if self.number > 2147483647 or self.number < -2147483647:
            return True

class Integer:

    @classmethod
    def input_digit(cls):
        error = 0
        try:
            number = input("input a num").strip()

            if not number.isdigit():
                error = 1
                print("invalid number")
                raise ValueError("invalid number")

            if SlopOverError(int(number), "越界").verify_slop_over():
                error = 1
                print("slop over")
                raise SlopOverError(number, "slop over")

        finally:
            return int(number) if error == 0 else cls.input_digit()


digit = Integer.input_digit()


