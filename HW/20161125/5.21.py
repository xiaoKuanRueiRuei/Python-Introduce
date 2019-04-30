for i in range (8):
    for j in range(7-i):
        print("%4s"%"",end=" ")
    for q in range(i+1):
        print("%4s"%2**(q),end=" ")
    for k in range(i):
        print("%4s"%2**(i-k-1),end=" ")
    print()