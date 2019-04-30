import random
n=10
a=random.sample(range(100),n)
#"取亂數"


def selection_sort(a):
    n=len(a)
    for i in range(0,n-1):
        k=i
        for j in range(i+1,n):
            if a[j]<a[k]:
                k=j
        
        #swap a[i],a[k]
        a[i],a[k]=a[k],a[i]
    return
#The main programming
#input selection_sort(a)
#and then input a 
#cantorl c-->stop

#The building Funcion of Python about selection sort
#input a=random.sample(range(10**10),100)
#and then input a.sort()
#finally input a
#we'll know the result