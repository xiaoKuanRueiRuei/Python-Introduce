a=[1,25,3,68,9]


def min(a):
    x=a[0]
    for i in range(1,len(a)):
        if a[i]<x:
            x=a[i]
    return x

def max(a):
    x=a[0]
    for i in range(1,len(a)):
        if a[i] > x:
            x=a[i]
    return x