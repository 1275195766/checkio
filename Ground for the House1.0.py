def house(plan):
    #replace this for solution
    plan=plan.split()

    print('plan '+str(plan))
    for i in range(len(plan)):
        h=len(plan)

        if plan[0].isdecimal():
            plan.remove(plan[0])
        elif plan[h-1].isdecimal():
            plan.remove(plan[h-1])


    cplan=[]
    for p in plan:
        cplan.append(list(p))
    print('cplan    '+str(cplan))
    if cplan==[]:
        return 0

    w=len(cplan[0])
    h=len(cplan)
    print(w,h)

    for l in range(w):
        n = 0
        m = 0
        w1=len(cplan[0])

        for i in range(w1):
            flog = 0

            for j in range(h):

                if cplan[j][i]=='0':
                    flog+=1
            print('flog    '+str(flog))
            if flog==h:
                n=i
                m=flog
        if m==h:
            for k in range(h):
                del cplan[k][n]


    print(cplan)

    print(len(cplan[0])*len(cplan))

    return len(cplan[0])*len(cplan)

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
