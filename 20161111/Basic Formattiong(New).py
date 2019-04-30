n=10
a=[(x,x**2,x**3)for x in range(1,n+1)]

for x, y, z in a :
    print('{:>5} {:>5} {:>5}'.format(x,y,z))