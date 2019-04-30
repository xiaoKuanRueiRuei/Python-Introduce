def binaryToDecimal(binaryString):
    a=0
    n=0
    while binaryString != 0:
        a = a + ((binaryString % 10)*(2**n))
        binaryString = binaryString // 10
        n+=1
    print(a)        