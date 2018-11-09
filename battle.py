class Weapon(object):
    def __init__(self, attack=5, range=1, fading=0.0):
        self.attack = attack
        self.range = range
        self.fading = fading

class Sword(Weapon):
    def __init__(self):
        super().__init__(attack=5)


class LongSword(Weapon):
    def __init__(self):
        super().__init__(attack=7)


class TwoHandedSword(Weapon):
    def __init__(self):
        super().__init__(attack=9, range=2, fading=0.9)


class Teeth(Weapon):
    def __init__(self):
        super().__init__(attack=4)


class ShortSword(Weapon):
    def __init__(self):
        super().__init__(attack=3)

class Knife(Weapon):
    def __init__(self):
        super().__init__(attack=1)


class Spear(Weapon):
    def __init__(self):
        super().__init__(attack=6, range=2, fading=0.5)

class Warrior(object):
    @property
    def is_alive(self):
        return 0 < self.health

    def __init__(self,
                 health=50,
                 attack=0,
                 defense=0,
                 vampirism=0.0,
                 weapon=Sword(),
                 heal=0):
        self.health = health
        self.healthMax = health
        self.defense = defense
        self.vampirism = vampirism
        self.weapon = weapon
        self.attack = attack
        self.heal = heal
    
    def striked(self, attacker, cover=0, line=0):
        if attacker.attack != 0: attacker.weapon=Weapon(attack=attacker.attack)
        damage = max(
            0, attacker.weapon.attack -
            (attacker.weapon.attack * attacker.weapon.fading) * line -
            self.defense - cover)
        self.health -= damage
        if self.health < 0:
            damage += self.health
            self.health = 0
        attacker.health += damage * attacker.vampirism

    def fight(self, other):
        while self.is_alive and other.is_alive:
            other.striked(self)
            if other.is_alive:
                self.striked(other)
    
    def healing(self, healer):
        self.health+=healer.heal


class Knight(Warrior):
    def __init__(self):
        super().__init__(weapon=LongSword())

class Healer(Warrior):
    def __init__(self):
        super().__init__(weapon=Knife(), heal=2)

class Rookie(Warrior):
    def __init__(self):
        super().__init__(attack=1)

# class Rookie(Warrior):
#     def __init__(self):
#         super().__init__()
#         self.health = 50
#         self.attack = 1

class Defender(Warrior):
    def __init__(self):
        super().__init__(weapon=ShortSword(), health=60, defense=2)

class Vampire(Warrior):
    def __init__(self):
        super().__init__(weapon=Teeth(), health=40, vampirism=0.5)

class Lancer(Warrior):
    def __init__(self):
        super().__init__(weapon=Spear(),health=50)

class Army(object):
    def __init__(self):
        self.army_units = []

    def add_units(self, klass, count=1):
        for idx in range(count):
            self.army_units.append(klass())

    def units(self):
        return iter(self.army_units)


# class Battle2(object):
#     def fight(self, left_army, right_army):
#         left = left_army.units()
#         right = right_army.units()

#         left_unit = next(left)
#         right_unit = next(right)
#         try:
#             while True:
#                 if left_unit.fight(right_unit):
#                     right_unit = next(right)
#                 else:
#                     left_unit = next(left)
#         except StopIteration:
#             pass

#         return left_unit.is_alive


class Battle(object):
    def fight(self, left_army, right_army):
        print ('{:>10} VS {:<10}'.format(
            'left_army','right_army'))
        left = left_army.army_units[:]
        right = right_army.army_units[:]

        while left[0].is_alive and left and right and right[0].is_alive:
            print('{:>10} vs {:<10}'.format(
                "".join(
                    list(map(lambda x: x.__class__.__name__[:1], left))[::-1]),
                "".join(list(map(lambda x: x.__class__.__name__[:1], right)))))
        
            while left[0].is_alive and right[0].is_alive:
                for line in range(min(left[0].weapon.range,len(right))):
                    right[line].striked(left[0], right[line - 1].defense if line > 0 else 0, line)
                if len(left)>1: left[0].healing(left[1])

                if right[0].is_alive:
                    for line in range(min(right[0].weapon.range,len(left))):
                        left[line].striked(right[0], left[line - 1].defense if line > 0 else 0, line)
                    if len(right) > 1: right[0].healing(right[1])
                            
            if not right[0].is_alive:
                right.pop(0)
            else:
                left.pop(0)

            if not right or not left:
                break


        print('{:>10} vs {:<10}'.format(str(bool(left)), str(bool(right))))
        print ()
        return (bool(left))


def fightb(one, second):
    while one[0].is_alive and second[0].is_alive:
        for x in range(len(second)):
            second[x].striked(one[0], second[x-1].defense if x>0 else 0, x)
        if second[0].is_alive:
            for x in range(len(one)):
                one[x].striked(second[0], one[x-1].defense if x>0 else 0, x)
    return one[0].is_alive

def fight(one, second):
    while one.is_alive and second.is_alive:
        second.striked(one)
        if second.is_alive:
            one.striked(second)
    return one.is_alive


if __name__ == "__main__":

    # unit1 = Warrior()
    # unit2 = Knight()
    # print (f"unit1 vs unit2 is win: ", unit1.fight(unit2))
    # print (unit1.weapon.__class__.__name__, unit1.weapon.attack , unit1.weapon.range)

    my_army = Army()
    my_army.add_units(Lancer, 1)
    my_army.add_units(Vampire, 1)
    my_army.add_units(Defender, 2)
    my_army.add_units(Lancer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Lancer, 1)
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 3)
    enemy_army.add_units(Vampire, 3)
    battle = Battle()

   # assert battle.fight(my_army, enemy_army) == False

    roo = Rookie()
    deff = Defender()
    assert fight(deff, roo) == True
    print (deff.health)

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

   # assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False

