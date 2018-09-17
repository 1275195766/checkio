class Warrior:
    def __init__(self):
        self.hp=50
        self.at=5
        self.is_alive=True

class Knight(Warrior):
    def __init__(self):
        super(Knight,self).__init__()
        self.at=7

def fight(unit_1, unit_2):
    flog=unit_1

    while True:
        if flog==unit_1 and unit_1.at==7:
            unit_2.hp-=7
            flog=unit_2
        elif flog==unit_2 and unit_2.at==7:
            unit_1.hp-=7
            flog=unit_1
        elif flog==unit_1 and unit_1.at==5:
            unit_2.hp -= 5
            flog = unit_2
        elif flog == unit_2 and unit_2.at == 5:
            unit_1.hp -= 5
            flog = unit_1

        if unit_1.hp<=0 and unit_2.hp>0:
            unit_1.is_alive=False

            break
        elif unit_2.hp<=0 and unit_1.hp>0:
            unit_2.is_alive=False

            break


    return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
