def guess_age(stand_age):
    print("You need guess my age now.")
    age = input("Please enter a age .If you want to quit, please enter 'q'.")
    while age != 'q':
        if int(age) < stand_age:
            age = input("it's too young.Please input again")
        elif int(age) > stand_age:
            age = input("it's too old.Please input again")
        else:
            print("You are right!!")
            break


age = 43
guess_age(age)
