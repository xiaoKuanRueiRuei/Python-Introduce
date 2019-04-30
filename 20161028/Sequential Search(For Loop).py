def sequential_search(a,x):
    for i in range(len(a)):
       if x ==a[i]:
           return i
    return -1
    
#input data=[4,8,1,7,9,6,3,10,5,2]
#key=7
#input sequential_search(data,key)
#We'll get the result:3
#so we'll know the number "7" is the 3rd number(4rd) in Python of data
#input sequential_search(data,20)
#We'll get the result:-1
#so the number "20" isn't in this data