def Binary_serch(a,x):
    index,left,right=-1,0,len(a)-1
    while left<=right and index<0:
        mid=(left+right)//2
        print('L={},R={},M={},DATA[M]={}'.format(left,right,mid,a[mid]))
        if x ==a[mid]:
            index=mid
        elif x<a[mid]:
            right=mid-1
        else:
            left=mid+1
    return index