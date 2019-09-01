
commoditys_list = []
with open("shopping.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        commoditys_list.append(line.split(','))

total = 0
for commondity in commoditys_list:
    total+=int(commondity[1]) * int(commondity[2])
print(total)

commonditys_information = []

for i in commoditys_list:
    commondity_information = {}

    commondity_information["name"] = i[0]
    commondity_information["price"] = i[1]
    commondity_information["count"] = i[2]
    commonditys_information.append(commondity_information)


res = filter(lambda x: int(x["price"]) >10000, commonditys_information)
print(list(res))
