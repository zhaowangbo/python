import random

def rand():
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', "P", 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    verification_code = []
    for i in range(8):
        n = random.randint(0, 1)
        if n == 0:
            verification_code.append(random.choice(number))
        else:
            verification_code.append(random.choice(alphabet))

    return verification_code


a = rand()
print(a)
