#n=10
a=[x for x in range(1,n+1)]
b=[x**2 for x in a]
c=[x**3 for x in a]

for i in range(n):
    print('%5d %5d %5d'%(a[i],b[i],c[i]))