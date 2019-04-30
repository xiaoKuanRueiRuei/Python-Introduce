def factors(n):
    print('%d: '%n,end='')
    i=2
    while i<=n:
        if n%i==0:
            while n%i==0:
                n//=i
            if n>1:
                print(i,end=", ")
            else:
                print(i)
                i+=1