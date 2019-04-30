a=[ float(x) for x in input("Enter numbers:").split()]

def mean(x):
    b = sum(x) / len(x)
    print("The mean is ", b)
    
def deviation(x):
    c=[]
    d=sum(a)/len(a)
    for x in range (0,len(a)):
        e=(a[x]-d)**2
        c.append(e)
    f=sum(c)/(len(c)-1)
    print('deviation=',f**0.5)
 
mean(a)
deviation(a)    