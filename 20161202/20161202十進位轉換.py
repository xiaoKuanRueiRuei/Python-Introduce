#迴圈
def from_base1(a,b):
    s=""
    while a>0:
        s=str(a%b)+s
#str即數字轉字串
        a//=b
    return s


#10進位轉成其他的 - 擴充(和上面程式超級像)
import string
#string字串程式庫
def from_base36_2(a,b):
    code=string.digits+string.ascii_uppercase
#digits-->0-9
#uppercase-->A~Z
#lowercase-->a~z
    s=""
    while a>0:
        s=code[a%b]+s
        a//=b
    return s


#迴圈
def from_base2(a,b):
    n=0
    for i in range (len(a)):
        n*=b
        n+=int(a[i])
    return n


#擴充(和上面程式超級像)
#import string(應該要寫，可是前面寫過的，所以這邊省略)
#string字串程式庫
def from_base36_1(a,b):
    code=string.digits+string.ascii_uppercase
#digits-->0-9
#uppercase-->A~Z
#lowercase-->a~z
    n=0
    for i in range(len(a)):
        n*=b
        n+=code.index(a[i])
#因為有字母，所以從code裡面轉進來(index式搜尋串列裡面資料，如果正確，就把位置傳回來)
    return n    


#遞迴
def from_base3(a,b):
    if a== 0:
        return ''
        #因為a已經預設為>0，所以如果=0表示結束了，所以傳回空字串
    return from_base3(a//b,b)+str(a%b)


#google code jam Practice
def alien():
    k=int(input())
    for i in range (k):
        a,code,to_code=input().split
        s= to_alien(from_alien(a,code),to_code)
        print("Case #{}: {}".format(i+1,s))

def from_alien(a,code):
    b=len(code)
    n=0
    for i in range(len(a)):
        n*=b
        n+=code.index(a[i])

def to_alien(a,code):
    b=len(code)
    s=""
    while a>0:
        s=code[a%b]+s
        a//=b
        return s