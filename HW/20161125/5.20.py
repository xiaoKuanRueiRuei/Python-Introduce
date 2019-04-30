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