def sequential_search(a,x):
    index=-1
    i=0
    while i < len(a):
        if x==a[i]:
            index=i
            break
        i+=1
    return index