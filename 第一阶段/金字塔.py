def pyramid(num):
    for i in range(num):
        for j in range(num - 1 - i):
            print(" ", end='')
        print("*"*(2 * (i+1) - 1))

for i in range(3):
    print("a")
for i in range(3):
    print("a", end='')