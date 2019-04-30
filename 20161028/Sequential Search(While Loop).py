def sequential_search(a,x):
    i=0
    while i<len(a):
        if x==a[i]:
            return i
        i+=1
    return -1
#one in two out