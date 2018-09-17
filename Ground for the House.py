def house(plan):
    #replace this for solution
    plan=plan.split()

    cplan=plan
    for p in cplan:
        if p.isdecimal():
            plan.remove(p)
    plan=[p[::-1] for p in plan]
    plan=[list(row) for row in zip(*plan)]
    cplan1=[]
    for i in plan:
        print(i)
        cplan1.append(''.join(i))
    for cp in cplan1:
        if cp.isdecimal():
            cplan1.remove(cp)
    print('plan' + str(cplan1))
    w=len(cplan1[0])
    h=len(cplan1)
    print(w,h)
    return w*h

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
