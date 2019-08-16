goods_dict ={"apple": 10, "mac": 10000, "iphone": 8000, "lenovo": 3000, "chicken": 10}
goods_buy = {}

print("Here are our goods and theirs prices")
for key, value in goods_dict.items():
    print(key, value)


while True:
    goods = input("please choose a good and enter the num you want to buy.Enter 'q' to quit")

    if goods =='q':
        break
    goods = goods .split(" ")
    if goods[0] not in goods_dict.keys():
        print(goods[0] + ": we don't have them")
        continue
    if len(goods) == 1:
        print("you forget to enter the num you want to buy")
        continue
    if not goods[1].isdigit():
        print("you need to input right price")
        continue

    goods_buy.update({goods[0]: int(goods[1])})

print("the goods you buy")
for key, value in goods_buy.items():
    print(key, value)

prices = 0
for good in goods_buy.keys():
    prices = prices + goods_buy[good] * goods_dict[good]
print("Total prices: ", prices)