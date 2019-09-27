#
# class Hero:
#     def __init__(self, name, level, hp, Q_hurt, W_hurt, E_hurt):
#
#         self.name = name
#         self.level = level
#         self.hp = hp
#         self.Q_hurt = Q_hurt
#         self.W_hurt = W_hurt
#         self.E_hurt = E_hurt
#
#     def Q(self, Enemy):
#         Enemy.hp -= self.Q_hurt
#         print("{}hp - {}".format(Enemy.name, self.Q_hurt))
#         if Enemy.hp <= 0:
#             print("{} has dead".format(Enemy.name))
#
#     def E(self, Enemy):
#         Enemy.hp -= self.E_hurt
#         print("{}hp - {}".format(Enemy.name, self.E_hurt))
#         if Enemy.hp <= 0:
#             print("{} has dead".format(Enemy.name))
#
#     def W(self, Enemy):
#         Enemy.hp -= self.W_hurt
#         print("{}hp - {}".format(Enemy.name, self.W_hurt))
#         if Enemy.hp <= 0:
#             print("{} has dead".format(Enemy.name))
#
#
# a = Hero("zhao", 15, 100, 10, 20, 30)
# b = Hero("wang", 15, 90, 10, 20, 30)
# a.W(b)
# a.W(b)
# a.W(b)
# a.W(b)
# a.W(b)
# print(b.hp)

import random

class Hero:
    def __init__(self, name, q_hurt=30, w_hurt=50, e_hurt=70, level=1, life=800):
        self.name = name
        self.level = level
        self.life = life
        self.is_active = True
        self.Q_hurt = q_hurt
        self.W_hurt = w_hurt
        self.E_hurt = e_hurt
        self.kill_count = 0

    def attack(self, skill, enemy):
        if self.name == enemy.name:
            return
        if self.life == False or enemy.life == False:
            return

        if enemy.life >= 0:
            enemy.life -= skill
        if enemy.life <= 0:
            enemy.life = 0
            enemy.is_activ = False
            self.kill_count += 1
            print("{} kill {}, has killed {}".format(self.name, enemy.name, self.kill_count))

            return enemy.is_active, self.kill_count

    def elevate(self):
        if self.kill_count % 5 == 0 and self.kill_count != 0:
            self.level += 1
            self.Q_hurt += 10
            self.E_hurt += 10
            self.W_hurt += 10
            print("level to {}".format(self.level))
            return self.level


obj1 = Hero('小1')
obj2 = Hero('小2')
obj3 = Hero('小3')
obj4 = Hero('小4')
obj5 = Hero('小5')

skill_dict = {
    'q_hurt': 30,
    'w_hurt': 50,
    'e_hurt': 70
}

for i in range(1000):
    random_obj1 = random.choice([obj1, obj2, obj3, obj4, obj5])
    random_obj2 = random.choice([obj1, obj2, obj3, obj4, obj5])
    random_skill = random.choice([skill_dict['q_hurt'], skill_dict['w_hurt'], skill_dict['e_hurt']])
    random_obj1.attack(random_skill, random_obj2)
    random_obj1.elevate()
