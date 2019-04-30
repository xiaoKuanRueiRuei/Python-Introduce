a=[x for x in range (1,11)]
def mean(a):
    return sum(a)/len(a)

def Var(a):
    u=mean(a)
    return sum((x -u)**2 for x in a)/len(a)

def Sta(a):
    return Var(a)**0.5

#for x in a 二段式論述

#The following is sample
def sample_Var(a):
    n=len(a)
    return Var(a)*n/(n-1)
