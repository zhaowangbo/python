def guess_age(age):
    i = 0
    while i < 3:
        print("you only have {0:d} chances".format(3 - i))
        input_age = input("please enter the age you guess")

        if int(input_age) != age:
            print("it is not right")

            if int(input_age) < age:
                print("it's too young.")
            else:
                print("it's too old.")

            i += 1

            if i == 3:
                continue_or_not = input("if you want to play again, enter'Y' or 'y'." +
                                        "And if you dont want to play again, enter 'N' or 'n'.")
                if continue_or_not == 'Y' or continue_or_not == 'y':
                    i = 0
                elif continue_or_not == 'N' or continue_or_not == 'n':
                    break
        else:
            print("You are right!!")
            break


right_age = 22
guess_age(right_age)