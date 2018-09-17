import time
def sun_angle(tim):
    #replace this for solution
    list=tim.split(':')

    if 360<=int(list[0])*60+int(list[1])<=1080:
        if int(list[1])==0:
            return (int(list[0])-6)*15
        else:
            tem=(int(list[0])-6)*15
            tem+=int(list[1])*0.25
            return tem
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")