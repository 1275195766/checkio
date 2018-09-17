def to_encrypt(text, delta):
    #replace this for solution
    translated=''
    for str in text:
        if str.isalpha():
            num=ord(str)
            num=num+delta
            if str.isupper():
                if num>ord('Z'):
                    num-=26
                elif num<ord('A'):
                    num+=26
            elif str.islower():
                if num >ord('z'):
                    num-=26
                elif num<ord('a'):
                    num+=26
            translated+=chr(num)
        else:
            translated+=str
    
    return translated

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")