#Sequential Serch 循序搜尋法、暴力法
#沒有任何技巧
#直接硬幹
#換句話說一次只能刪除掉一個資料

#Binary Serch     二分搜尋法(前提是DATA要先排好順序)-->從一半開始剖析
#換句話說比較一次可以刪除掉一半資料
#例如有10筆資料
#位置為0123456789
#則0+9//2=4
#發現所求於又或左側
#如果在右側則+1再//
#座側則-1再//
#如果全部搜尋完以後發現沒有
#那就表示所求不在資料中
#因為要知道資料數量，所以可以先用lense函數，只是len()=n是資僚長度，位置要n-1
#期末考可能會考
#迴圈
def Binary_serch1(a,x):
    index,left,right=-1,0,len(a)-1
    while left<=right and index<0:
        mid=(left+right)//2
        print('L={},R={},M={},DATA[M]={}'.format(left,right,mid,a[mid]))
        if x == a[mid]:
            index=mid
        elif x < a[mid]:
            right=mid-1
        else:
            left=mid+1
    return index

#遞迴 
def Binary_serch2(data,key,left,right):
    if left>right:
        return -1
#因為已經排序過了
#所以如果左邊大於右邊
#表示這個DATA是不是用於二分搜尋法的
        mid=(left+right)//2
        print('L={},R={},M={},DATA[M]={}'.format(left,right,mid,data[mid]))
        if key == data[mid]:
            return mid
        elif key < data[mid]:
            return Binary_serch2(data,key,left,mid-1)
        else:
            return Binary_serch2(data,key,mid+1,right)

#>>>data=[12,23,43,45,56,87,91]
#>>>data.sort()
#>>>key=43
#>>>Binary_serch(data,key)



#Divide and Conquer Algorithm  策略搜尋法
#經常搭配遞迴
def min(data,low,high):
    if low==high:
        return data[low]

    mid=(low+high)//2
    x=min(data,low,mid)
    y=min(data,mid+high)
#這邊的low,high,mid是指位置不是指值
#因為直是我們要求的    
    return x if x<y else y
#>>>a=[2,4,9,-10,1,999,0]
#>>>min(a,0,len(a)-1)
#-10
