def sequential_search(a,x):
    index=-1
    i=0
    while i < len(a) and index < 0 :
        if x==a[i]:
            index=i
        i+=1
    return index
    
    
    
    
#資料所在位置用index