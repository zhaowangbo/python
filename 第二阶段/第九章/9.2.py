
names = ['albert', 'jr_shenjing', "kobe", "kd"]

name = list(filter(lambda n: n.endswith("shenjing"), names))

names.remove(name[0])
print(names)
