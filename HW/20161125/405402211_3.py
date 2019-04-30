#5.3
print("kilograms      Pounds")

for x in range(1,200,2):
    print("%-9d      %6.1f"%(x,x*2.2))
    
#5.4
print("Miles      Kilometers")

for x in range(1,11,1):
    print("%-2d         %2.3f"%(x,x*1.609))
    
    
#5.12
i=int(input("100到1000區間:"))
b=1
c=0
while b in range(1,i):
    if b%5==0 or b%6==0 :
        print(b,end=" ")
        b+=1
        c+=1
        if c%10==0:
           print("")
    else:
        b+=1
 
        
        
#5.13
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

        
#5.18
def factors(n):
    print('%d= '%n,end='')
    i=2
    while i<=n:
        while n%i==0:
            n//=i
            if n>1:
                print(i,end=" , ")
            else:
                print(i)
        i+=1


#5.20
print("Pattern A")
for a in range (7):
    for b in range(1,1+a):
        print(b,end=" ")
    print()

    
print("Pattern B")
print(" ")
for c in range (7):
    for d in range(1,7-c):
        print(d,end=" ")
    print()

    
print("Pattern C")
for e in range (7):
    for f in range(7-e-1):
        print(" ",end=" ")
    for g in range(1,e+1):
        print(e-g+1,end=" ")
    print()

print("Pattern D")
print("")
for h in range (7):
    for i in range(0+h):
        print(" ",end=" ")
    for j in range(1,7-h):
        print(j,end=" ")
    print()
  

#5.21
for i in range (8):
    for j in range(7-i):
        print("%4s"%"",end=" ")
    for q in range(i+1):
        print("%4s"%2**(q),end=" ")
    for k in range(i):
        print("%4s"%2**(i-k-1),end=" ")
    print()