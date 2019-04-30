i=int(input("100到1000區間:"))
b=1
c=0
while b in range(1,i):
    if (b%5==0 and b%30!=0) or (b%6==0 and b%30!=0):
        print(b,end=" ")
        b+=1
        c+=1
        if c%10==0:
           print("")
    else:
        b+=1