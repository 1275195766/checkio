from typing import List

def checkio(list):
    str=''.join(list)
    bo=[s for s in str]
    
    if  ((bo[6] == 'O' and bo[7] == 'O' and bo[8] == 'O')  # 顶部连成一条线
        or (bo[3] == 'O' and bo[4] == 'O' and bo[5] == 'O')  # 中部连成一条线
        or (bo[0] == 'O' and bo[1] == 'O' and bo[2] == 'O')  # 底部连成一条线
        or (bo[6] == 'O' and bo[3] == 'O' and bo[0] == 'O')  # 左边连成一条线
        or (bo[7] == 'O' and bo[4] == 'O' and bo[1] == 'O')  # 中间连成一条线
        or (bo[8] == 'O' and bo[5] == 'O' and bo[2] == 'O')  # 右边连成一条线
        or (bo[6] == 'O' and bo[4] == 'O' and bo[2] == 'O')  # 斜线
        or (bo[8] == 'O' and bo[4] == 'O' and bo[0] == 'O')):  # 斜线
        a='O'
    elif ((bo[6] == 'X' and bo[7] == 'X' and bo[8] == 'X')  # 顶部连成一条线
        or (bo[3] == 'X' and bo[4] == 'X' and bo[5] == 'X')  # 中部连成一条线
        or (bo[0] == 'X' and bo[1] == 'X' and bo[2] == 'X')  # 底部连成一条线
        or (bo[6] == 'X' and bo[3] == 'X' and bo[0] == 'X')  # 左边连成一条线
        or (bo[7] == 'X' and bo[4] == 'X' and bo[1] == 'X')  # 中间连成一条线
        or (bo[8] == 'X' and bo[5] == 'X' and bo[2] == 'X')  # 右边连成一条线
        or (bo[6] == 'X' and bo[4] == 'X' and bo[2] == 'X')  # 斜线
        or (bo[8] == 'X' and bo[4] == 'X' and bo[0] == 'X')):  # 斜线
        a='X'
    else:
        a='D'

    return a

if __name__ == '__main__':
    print("Examp'O':")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding comp'O'te? Click 'Check' to review your tests and earn cool rewards!")