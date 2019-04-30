a=[str(x) for x in input('Enter integers between 1 and 100:').split()]
a.sort()
while a  != []:
    b=a.count(a[0])
    if b>1:
        print(a[0],'occurs',b,'times')
    else:
        print(a[0],'occurs',b,'time')
    for _ in range (b):
        a.remove(a[0]) 

    
        
        




