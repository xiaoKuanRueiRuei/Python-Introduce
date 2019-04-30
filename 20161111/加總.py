k=int(input())
    for in range(k):
    a,b=[int(x)for x in input().split()]
    s=sum(x for x in range(a,b+1))
    print('sum({}, {}))={}'.format(a,b,s))