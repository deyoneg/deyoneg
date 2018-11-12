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

    @property
    def attack(self):
        return self.weapon.attack

    @attack.setter
    def attack(self, value):
        self.weapon = Weapon(attack=value)

    def __init__(self,
                health=50,
                defense=0,
                vampirism=0.0,
                weapon=None,
                heal=0):
        self.health = health
        self.healthMax = health
        self.defense = defense
        self.vampirism = vampirism
        self.weapon = weapon
        self.heal = heal
        if weapon is None:
            self.weapon = Sword()

    def confirm_produced_damage(self, damage):
        self.health += damage * self.vampirism

    def get_striked(self, attacker, cover=0, line=0):
        damage = max(
            0, attacker.weapon.attack - (attacker.weapon.attack * attacker.weapon.fading) * line -
            self.defense - cover)
        self.health -= damage
        damage = min(self.health, damage)
        attacker.confirm_produced_damage(damage)
        return self.is_alive

    def fight(self, other):
        while self.is_alive and other.is_alive:
            if other.get_striked(self):
                self.get_striked(other)
        return self.is_alive

    def healing(self, healer):
        self.health += healer.heal

class Knight(Warrior):
    def __init__(self):
        super().__init__(weapon=LongSword())


class Healer(Warrior):
    def __init__(self):
        super().__init__(weapon=Knife(), heal=2)


class Rookie(Warrior):
    def __init__(self):
        super().__init__(attack=1)

#! временное явления изза особенностей тестового класса на checkio
#! ВОт такой там проверочный класс. как его атаку сканверторовать в weapon
#! в конструкторе класса я хз. 
class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 1

class Defender(Warrior):
    def __init__(self):
        super().__init__(weapon=ShortSword(), health=60, defense=2)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(weapon=Teeth(), health=40, vampirism=0.5)


class Lancer(Warrior):
    def __init__(self):
        super().__init__(weapon=Spear(), health=50)


class Army(object):
    # def __str__(self):
    #     pass

    def __init__(self):
        self.army_units = []

    def add_units(self, klass, count=1):
        for idx in range(count):
            self.army_units.append(klass())

    def units(self):
        return iter(self.army_units)


class Battle(object):
    def fight(self, left_army, right_army):
        print('{:>10} VS {:<10}'.format(
            'left_army', 'right_army'))
        left = left_army.army_units[:]
        right = right_army.army_units[:]

        while left and right and left[0].is_alive and right[0].is_alive:
            print('{:>10} vs {:<10}'.format(
                "".join(
                    list(map(lambda x: x.__class__.__name__[:1], left))[::-1]),
                "".join(list(map(lambda x: x.__class__.__name__[:1], right)))))

            #! красивый цикля я еще не придумал, пока что для меня более понятный.
            while left[0].is_alive and right[0].is_alive:
                for line in range(min(left[0].weapon.range, len(right))):
                    right[line].get_striked(left[0], right[line - 1].defense if line else 0, line)
                #! как лучше сделать? чтоб объект когото лечил? или чтоб его личили кем то?
                if len(left) > 1: left[0].healing(left[1]) 

                if right[0].is_alive:
                    for line in range(min(right[0].weapon.range, len(left))):
                        left[line].get_striked(right[0], left[line - 1].defense if line else 0, line)
                    if len(right) > 1: right[0].healing(right[1])

            #! куда лучше запихнуть уборку трупов?
            left = self.removeDeadBodies(left)
            right = self.removeDeadBodies(right)

            if not right or not left:
                break

        print('{:>10} vs {:<10}'.format(str(bool(left)), str(bool(right))))
        print()
        return (bool(left))

    def removeDeadBodies(self,remainSoldiers):
        for i,u in enumerate(remainSoldiers):
            if not u.is_alive:
                remainSoldiers.pop(i)
        return remainSoldiers

# def fightb(one, second):
#     while one[0].is_alive and second[0].is_alive:
#         for x in range(len(second)):
#             second[x].get_striked(one[0], second[x - 1].defense if x > 0 else 0, x)
#         if second[0].is_alive:
#             for x in range(len(one)):
#                 one[x].get_striked(second[0], one[x - 1].defense if x > 0 else 0, x)
#     return one[0].is_alive


def fight(one, second):
    while one.is_alive and second.is_alive:
        second.get_striked(one)
        if second.is_alive:
            one.get_striked(second)
    return one.is_alive


if __name__ == "__main__":
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

    assert battle.fight(my_army, enemy_army) == False

    roo = Rookie()
    deff = Defender()
    assert fight(deff, roo) == True
    print(deff.health)

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

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Healer, 2)
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

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
