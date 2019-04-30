def decimalToBinary(value):
    a=0
    i=0
    while value != 0:
        a = a + value % 2 * 10**i
        value = value // 2
        i+=1
    print(a)