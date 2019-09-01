person_list = []
with open("a.txt", 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        person = {}
        line = line.strip("\n").split(' ')
        person["name"] = line[0]
        person["sex"] = line[1]
        person["age"] = line[2]
        person["salary"] = line[3]
        person_list.append(person)

# print(person_list)

max_salary_person = max(person_list, key=lambda x: x["salary"])
min_age_person = min(person_list, key=lambda x: x["age"])
# print(max_salary_person)
# print(min_age_person)
name_map_list = map(lambda x: x["name"].title(), person_list)
a = list(name_map_list)


for i, person in enumerate(person_list):
    person["name"] = a[i]
# print(person_list)


name_res = filter(lambda x: x["name"][0]=='A', person_list)
print(person_list)
name_res = list(name_res)
for name in name_res:
    person_list.remove(name)

print(person_list)
