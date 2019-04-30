data=[int(x) for x in input('Enter data:').split()]
def mean(data):
    b=sum(data)/len(data)
    print('mean=',b)
def deviation(data):
    c=[]
    d=sum(data)/len(data)
    for x in range (0,len(data)):
        e=(data[x]-d)**2
        c.append(e)
    f=sum(c)/(len(c)-1)
    print('deviation=',f**0.5)
    
mean(data)
deviation(data)    
    
    
    
    
    
