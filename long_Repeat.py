def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    flog=1
    list=[]
    if line=='':
        return 0
    for i in range(len(line)-1):

        if line[i]==line[i+1]:
            flog=flog+1
        else:
            flog=1
        list.append(flog)
    # print(list)
    m=max(list)
    return m

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('AA')==2, "AA"
    print('"Run" is good. How is "Check"?')