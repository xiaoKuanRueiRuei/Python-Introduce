def bubble(x):
    l = len(x)        
    for a in range(l):
        for b in range(l-1):
            if (x[a] < x[b]):
                x[a], x[b] = x[b], x[a]
    return x 