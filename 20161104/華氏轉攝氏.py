c=[x for x in range(50,100+1,5)]
f=[9/5*x+32 for x in c]

for x,y in zip(c,f):
    print('{:>8.2f} {:>8.2f}'.format(x,y))