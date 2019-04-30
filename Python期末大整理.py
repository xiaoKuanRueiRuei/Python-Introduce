#判斷撲克牌花色和數字
def suit1(x):
    if x//13==0:
        print("S")
    elif x//13 ==1:
        print("H")
    elif x // 13==2:
        print("D")
    else:
        print("C")
        
def rank1(x):
    if x%13+1==1:
        y="A"
    elif x%13+1==11:
        y="J"
    elif x%13+1==12:
        y="Q"
    elif x%13+1==13:
        y="K"
    else:
        y=x%13+1
    print(y)


n=int(input("Please enter a number:"))
["S","H","D","C"][n//13]


def suit2(n):
    return ["S","H","D","C"][n//13]

#{1:"A",11:"J",12:"Q",13:"K"}.get(13, "hello")
#.get函式中，如果答案沒有在裡面，可在後面輸入標準答案
n=int(input("Please enter a number:"))
{1:"A",11:"J",12:"Q",13:"K"}.get(n%13+1, n%13+1)


#if the range from zoro , you can not write zero.


def rank2(n):
    x=n%13+1
    return {1:"A",11:"J",12:"Q",13:"K"}.get(x,str(x))


import random

def card(x):
    return suit2(x) + rank2(x)

def hand():
    a=random.sample(range(52),5)
    print(a)
    return [card(x) for x in a]
#Sorting Method


def flush2(a):
    b=sorted ([x[0] for x in a])
    print(b)
    return b.count(b[0])==5
#判定同花順


def flush3(a):
    c=sorted ([x[0] for x in a])
    print(c)
    return c.count(c[0])==4
#判定鐵支
#不跳行排版-->print("hola",end=" ")
#end的意思是這一個print的最後面不跳行，而且還加東西


#20161125
def four_of_a_kind(a):
    b=[x[1:] for x in a ]
    c=sum(b.count(x)for x in b)
    print('{}, count={}'.format(b,c))
    return c == 17
#the number of pair becuse 幾張一樣(2,1,1,1)，平方=2**2+1+1+1=7
#the number of fullhouse (3,2)，平方=3**2+2**2=13
#鐵支=(4,1)=4**2+1=17
#單張(1,1,1,1,1)=5
#三條(3,1,1)=3**2+1+1=11
#Two pair(2,2,1)=2**2+2**2+1=9

#Binary Search二分搜尋法
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
    
#Factorial
import sys
sys.setrecursionlimit(2000)
#支援大數據
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
#Fibonacci_Sequence(費氏數列)
def fib1(n):
    a,b=0,1
    for _ in range(n):#"_"是沒有意義的變數名稱
        a,b=b,a+b
    return a
    

from functools import lru_cache
@lru_cache(maxsize=1024)
def fib2(n):
    return n if n <=1 else fib2(n-1)+fib2(n-2)
#重複計算，因為沒有記憶之前算過的數字，上面兩行是加上記憶的功能(快取的暫存記憶)

#GCD
def gcd1(a,b):
    for i in range (1,min(a,b)+1):
        if(a%i==0) and (b%i==0):
            x=i
    return x
#千萬不要用


def gcd2(a,b):
    while b>0:
        a,b=b,a%b
    return a
#輾轉相除法


def gcd3(a,b):
    if b==0:
        return a
    
    return gcd3(b,a%b)
#遞迴(自己呼叫自己)
    

def gcd4(a,b):
    return a if b == 0 else gcd4(b,a%b)
#遞回，三元寫法

#密碼檢查
#any(iterable)
#Return Ture if any element of the iterable id ture.
#If the iterable is empty,return False.
#Equivalent to :
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
#input-->any(c.isupper() for c in "Hello")-->
#裡面有一個大寫就對了
#input-->any(c in ["!","@"."#","$"] for c in iPhone@Apple)-->
#iPhone@Apple是密碼，在密碼中有前述4個特殊字元，所以正確
#input-->all(c.isupper() for c in "Hello")-->
#裡面有一個大寫就錯了
#input-->all(c in ["!","@"."#","$"] for c in iPhone@Apple)-->
#iPhone@Apple是密碼，在密碼中有前述4個特殊字元，所以錯誤
#all跟any的差異在，any是只要一個有就可以了，all是要全部都符合才正確
def check_password(a):
    return all([
        any(c.isupper()for c in a),
        any(c.islower()for c in a),
        any(c.isdigit()for c in a),
        any(c in ["!","@","#","$"]for c in a),
        len(a)>=8])

#十進位轉換
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

#三大搜尋法
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

#進位內建
#3-36進位
int("number","進位")
#2進位
bin("number","進位")
#print"0bXXXXXXXXXXXXX"-->0b是指二進位
#8進位
oct("number","進位")
#print="0oXXXXXXXXXXXX"-->0o代表八進位
#16進位
hex("number","進位")

#整體變數與局部變數
#GLOBAL
def f():
    print(s)
    
#s is global
s = ' I love Paris!'
f()
# I love Paris!





#整體變數、局部變數
#s第一次出現在函數外
#在外面出現的資料叫"整體變數(Global)"





#LOCAL
def f():
    #s is local
    s = ' I love London!'
    print(s)
    
#s is global
s = ' I love Paris!'
f()
print(s)
# I love London!
# I love Paris!





#錯誤範例
def f():
    print(s)
    #s is local and global (ERROR!)
    s='I love London!'
    print(s)
    
#s is global
s='I love Paris!'
f()
print(s)
#UnboundLocalError: local variable 's' referenced before assignment
#Python是全部編譯後才執行
#對第一個print(s)而言
#s為global
#對第二個print(s)而言
#s為local
#因此發現順序有問題
#ERROR!
#常犯錯誤請記得!





#新指令gloabl
def f():
    global s
    print(s)
    s = 'I love London!'
    print(s)
    
#s is global
s='I love Paris!'
f()
print(s)
#I love Paris!
#I love London!
#I love London!
#最後一個print(s)
#因為跑過 s='I love London!'
#所以s='I love Paris!'被 s='I love London!'取代了
#為了避免這種狀況
#盡量避免global的用法





#錯誤範例
def f():
    s='I love London!'
    print(s)
    
f()
print(s)
#UnboundLocalError: local variable 's' referenced before assignment
#就是黑箱作業啦(封裝處理)!!!
#在程式中越黑越好
#這樣才不會相互干擾





#LOCAL Versus NONLOCAL
#LOCAL
def f():
    def g():
        s='I love Berlin!'
        print(s)
        
    def h():
        s='I love Rome!'
        print(s)
        
    s = 'I love London!'
    g()
    h()
    print(s)
    
s = 'I love Paris!'
f()
print(s)
#I love Berlin!
#I love Rome!
#I love London!
#I love Paris!

#g()、h()是f()的local function
#g()、h()的 s都是local
#所以不會被取代



#NONLOCAL
def f():
    def g():
        nonlocal s
        s='I love Berlin!'
        print(s)
        
    def h():
        nonlocal s
        s='I love Rome!'
        print(s)
        
    s = 'I love London!'
    g()
    h()
    print(s)
    
s = 'I love Paris!'
f()
print(s)
#I love Berlin!
#I love Rome!
#I love Rome!
#I love Paris!

#nonlocal將local變成f()中公有的
#因為nonlocal s
#所以g()開始往外面找
#這時找到f()
#找到s了!
#可是是s='I love Berlin!'-->第一個print
#而不是s = 'I love London!'
#因為s = 'I love London!'被s='I love Berlin!'取代了
#相同的道理執行h()
#此時原本取代London的Berlin又被Rome取代了
#這是第二個print
#在執行第三個print時
#因為Rome是最後一個s了
#因此再次輸出Rome
#最後一個print則是輸出Paris

#文字輸入輸出
#sample input:

#Jeremy Lin
#95 87 91
#Kobe Bryant
#86 96 73
#Michael Jordan
#89 91 80
#Larry Bird
#43 92 77
#Dirk Nowitzki
#76 75 96

#上面是文字檔

#檔案輸入
fn = 'sample.txt'
with open (fn,'r') as f:
    line = f.readlines()

data=[]
for i in range (0,len(line),2):
    name = line[i].strip()
    s = line[i+1].split()
    score = [int(x) for x in s]
    data.append((name,score))
#fn=File Name
#'r'指read
#只輸入不寫入
#as f 的 f是指檔案
#as 是取名的意思
#readlines指每一行都讀進來
#strip刪除多餘的字
#把字拆開
#沒有特別註明就當空白處理
#Note!頭尾拿掉-->srtip
#頭尾中間都要-->split
#刪除頭尾空白
#split用空白當空格
#將成績拆開來
#編號0是姓名
#編號1,3,5,7是成績
#i間隔是2
#是因為個人資料有兩筆
#如果個人資料有三筆
#間隔就是三
#以此類推
#int的處理是要將字串轉數字
#append的意思是附加檔案之意
#指說當成是處理完後
#附加上name和score的資料
#>>> data
#[('Jeremy Lin', [95, 87, 91]), ('Kobe Bryant', [86, 96, 73]), ('Michael Jordan', [89, 91, 80]), ('Larry Bird', [43, 92, 77]), ('Dirk Nowitzki', [76, 75, 96])]
#>>> score
#[76, 75, 96]
#>>> name
#'Dirk Nowitzki'
#score和name因為一次只處理一個人
#所以只有一個資料
#>>> line
#['Jeremy Lin\n', '95 87 91\n', 'Kobe Bryant\n', '86 96 73\n', 'Michael Jordan\n', '89 91 80\n', 'Larry Bird\n', '43 92 77\n', 'Dirk Nowitzki\n', '76 75 96']
#"\n"是一個看步道的符號，是換行字元





#檔案輸出(迴圈)
fn = 'output.txt'
with open (fn,'w')as f:
    for x in data:
        name,score = x
        total = sum(score)
        average = total / len(s)
        f.write('name = {} \n'.format(name))
        f.write('total = {} \n'.format(total))
        f.write('average = {:.2f} \n'.format(average))        
#w指write
#沒有寫輸出至哪裡
#就是輸出在河程式檔相同的儲存空間中
#:.2f是指取到小數點第二位
#.是指功能之意
#這邊的f是指float浮點數
#:.是舉到第幾位的意思
#{}這是輸出編排指令
#%功能比{}少
#%是舊的寫法
#{}是新的寫法
#大括號是文字編排
#format是指格式化的意思
#意思是將前面的隔是套在format括號中的東西





#新寫法
fn = 'sample.txt'
with open (fn,'r') as f:
    line = f.readlines()
    
name = [x.strip() for x in line[::2]]
score = [[int(x) for x in y.split()] for y in line[1::2]]
data = [(x,y) for x , y in zip(name , score)]
#[::2]把name從零開始間隔二的間隔strip掉
#[1::2]把data從零開始間隔二的間隔strip掉
#zip拉拉鏈的概念
#把東西配合起來
#>>> data
#[('Jeremy Lin', [95, 87, 91]), ('Kobe Bryant', [86, 96, 73]), ('Michael Jordan', [89, 91, 80]), ('Larry Bird', [43, 92, 77]), ('Dirk Nowitzki', [76, 75, 96])]
#>>> score
#[[95, 87, 91], [86, 96, 73], [89, 91, 80], [43, 92, 77], [76, 75, 96]]
#>>> name
#['Jeremy Lin', 'Kobe Bryant', 'Michael Jordan', 'Larry Bird', 'Dirk Nowitzki']
#>>> line
#['Jeremy Lin\n', '95 87 91\n', 'Kobe Bryant\n', '86 96 73\n', 'Michael Jordan\n', '89 91 80\n', 'Larry Bird\n', '43 92 77\n', 'Dirk Nowitzki\n', '76 75 96']
 
#演算法
#利用演算法找出最小值(很像20161202最後一個)
def min(a,low,high): #這裡的low跟high是位置
    if low == high: #只剩最後一人
        return a [low] #寫a[high]也可以

    mid = ( low + high ) // 2 
#人數超過一人
#因為是整數索引
#所以用//
    x = min( a , low , mid )
    y = min( a , mid+1 , high )
    
    return x if x < y else y
    
#>>>a=[2,4,9,-10,1,999,0]
#>>>min(a,0,len(a)-1)
#-10
#問題本質不變
#將資料劃分為左右各一半
#減少數量
#可用遞迴
#key:分而至至，大問題化為小問題但性質不變





#快速排序法(Quicksort)
def quicksort(a):
    if len(a)<=1:
        return a
    
    return quicksort([x for x in a[1:] if x < a[0]]) +\
        [a[0]] +\
        quicksort([x for x in a[1:] if x >= a[0]])

#[1:]從編號1(第二位，因為第一個數字(編號0)拿去當標兵了)
#照理說要[1:50](最後一個不算，所以是到編號49(第50位))
#可是因為是到最後面
#所以省略50
#如果是前面都算(要第1位到第20)
#[:21]

#+/是接續的意思
#因為式子太長了
#>>> a=[2,9,5,6,5,21,5646,523,541,51314,5466,56]
#>>> quicksort(a)
#[2, 5, 5, 6, 9, 21, 56, 523, 541, 5466, 5646, 51314]

#>>> a=random.sample(range(1000000),50)
#>>> a
#[752878, 706610, 797734, 943620, 166648, 278777, 836834, 393291, 376299, 293766, 6849, 293217, 74566, 615874, 273201, 872705, 885634, 106021, 983425, 502083, 287004, 56862, 772246, 115440, 608813, 518119, 960337, 78945, 716364, 465422, 166369, 358085, 828272, 47688, 874610, 915875, 466887, 423080, 499999, 943500, 140012, 415681, 692237, 149714, 633269, 969047, 941554, 280041, 388510, 744094]
#>>> b=quicksort(a)
#>>> b
#[6849, 47688, 56862, 74566, 78945, 106021, 115440, 140012, 149714, 166369, 166648, 273201, 278777, 280041, 287004, 293217, 293766, 358085, 376299, 388510, 393291, 415681, 423080, 465422, 466887, 499999, 502083, 518119, 608813, 615874, 633269, 692237, 706610, 716364, 744094, 752878, 772246, 797734, 828272, 836834, 872705, 874610, 885634, 915875, 941554, 943500, 943620, 960337, 969047, 983425]
#>>> c=sorted(a)
#>>> b==c
#True

#挑一個人當標兵
#比標兵矮的在左邊
#比標兵高的在右邊
#因為左邊跟右邊是沒有順序的
#因此左邊跟右邊用相同方法
#繼續快速排列





#Bisection Method(典型的二分法)
#選定一個區間
#因為conti.
#所以一正一負
#中間必有解
#即一個函數求解
#同正或同負就拋棄
def bisection(f,x1,x2,e = 1e-6):
    y1=f(x1)
    
    while x2 - x1 > e:
        x = (x1 + x2) / 2.0
        y = f(x)
        
        if y * y1 >0:
            x1 = x
        else:
            x2 = x
    return x
        
#Python把函數當參數傳回
#e代表誤差值
#1e的 e是指(10的n次方)
#1e-6 = 10的-6次方
#兩個 e不一樣
#浮點數用以科學記號表示法
#浮點數用/(一條斜線)
#x的位置(x1-->x-->x2)
#所以當y*y1>0時
#x右移

#>>> x=bisection(lambda x : x**2-3*x+2,0,1.5)
#>>> print('{:.3f}'.format(x))
#1.000

#>>> x=bisection(lambda x : x**2-3*x+2,1.5,3)
#>>> print('{:.3f}'.format(x))
#2.000

#lambda funcion是臨時函數
#":"後可直接寫你要用的式子

#Celsius class 套件
#基礎攝氏轉華氏的套件
class celsius:
    def __init__(self,t=0):
        self._t=t
        
    def c(self):
        return self._t
    
    def f(self):
        return 9/5*self._t+32
#期末考要自己會寫出類別來
#套件就是一個容器的概念
#套件中可以包含資料及指令
#self代表自己這個物件
#Python執行中會產生一指標
#self就是告訴Pytjon要用的指標就是自己
#t代表溫度，沒其他意思
#_底線指系統表示系統裡面的變數
#不可以去動他
#有底線開頭的程式
#表示外在程式不可以去動
#這是系統內部自行運用
#__雙底線是指絕對不能用哈哈
#init初始化(initilize)
#t=0是初值(內定參數)
#self._t = t將外面的t抄進去內部來，意思就是保留一份
#想要取得什麼資料
#就放進去變數中
#java有封裝
#而Python沒有
#>>> a=celsius(85)
#>>> a.c()
#85
#>>> a.f()
#185.0
#>>> a
#<__main__.celsius object at 0x00000000074E80F0>
#>>> a.f
#<bound method celsius.f of <__main__.celsius object at 0x00000000074E80F0>>
#>>> a.c
#<bound method celsius.c of <__main__.celsius object at 0x00000000074E80F0>>
#>>> a._t
#85





#員周與面積的套件
import math
class circle1():
    def __init__(self,r=1):
        self._r=r
        
    def area(self):
        return math.pi * (self._r)**2
        
    def perimeter(self):
        return  2 * math.pi * self._r
#>>> a=circle(2)
#>>> a.perimeter()
#12.566370614359172
#>>> a.area()
#12.566370614359172





#Celsius calss eith getters anf setters(Java寫法)
class celsius2:
    def __init__(self,t = 0):
        self._t=t
        
    def getc(self):
        return self._t
    
    def setc(self,t):
        self._t = max(-273,t)
    
    def getf(self):
        return 9/5*self._t+32
        
#-273度F是絕對零度
#也就是最低溫度了
#Python中把get , set拿掉了
#>>> a=celsius2(85)
#>>> a.getc()
#85
#>>> a.getf()
#185.0




#Python寫法的get , set
class celsius3:
    def __init__(self,t=0):
        self._t=t
        
    @property
    def c(self):
        return self._t
    
    @c.setter
    def c(self,t):
        self._t=max(-273,t)
    
    @property
    def f(self):
        return 9/5*self._t+32
#@是裝飾用
#有點像空屋中的裝潢
#他可以擴充其他功能
#但是就算不寫@
#基本功能依舊存在
#>>> a=celsius3(85)
#>>> a.c
#85
#>>> a.f
#185.0.
#>>> a
#<__main__.celsius2 object at 0x00000000074E8DA0>
#不用打()了!





#String(字串) representation(官方輸出指令，官方表示法) in Python:
    #__repr__goal is to be unambiguous
    #__str__goal is to be readable

    
class celsius4:
    def __init__(self,t=0):
        self._t=t
        
    @property
    def c(self):
        return self._t
    
    @c.setter
    def c(self,t):
        self._t=max(-273,t)
    
    @property
    def f(self):
        return 9/5*self._t+32
        
    def __repr__(self):
        return str(self._t)
#representation傳回的都是字串
#>>> a=celsius4(85)
#>>> a.c
#85
#>>> a.f
#185.0
#>>> print(a)
#85
#>>> a
#85


class celsius5:
    def __init__(self,t=0):
        self._t=t
        
    @property
    def c(self):
        return self._t
    
    @c.setter
    def c(self,t):
        self._t=max(-273,t)
    
    @property
    def f(self):
        return 9/5*self._t+32
        
    def __repr__(self):
        return str(self._t)
        
    def __str__(self):
        return str(self._t) + u'\N{DEGREE SIGN}c'
        
#u表示unicode
#>>> print(a)
#85°c
#>>> a
#85
#如果有寫str
#那print(a)時就會顯示是何人閱讀的方式
#即為剛剛寫的格式
#而a則是直接輸出Python內定的格式
#即為repr





#Vector class向量(發票即為此應用)
class Vector:
    def __init__(self,*args):
        if not args:
            self.values = (0,0)
        else:
            self.values = args
#以上為向量初始化寫法

#拆封
#Sequence unpacking 拆封的概念 
#>>> a=[3,7,1,4,2]
#>>> x,y,*z=a
#>>> x,y,z
#(3, 7, [1, 4, 2])
#>>> a='PYTHON'
#>>> x,y,*z=a
#>>> x,y,z
#('P', 'Y', ['T', 'H', 'O', 'N'])
#個體資料與總體資料的差意
#把總體分解為個體
#container這是一個容器的概念
#將資料當成書
#將串列視為書包
#如果知道有三個資料，當然可以寫成x,y,z=a
#但是只知道至少兩筆資料
#所以x,y可以直接寫出來
#*z是一個umpacking的寫法
#意思是不知道後面有多少資料
#全部塞到z裡面去
#所以由第二個PYTHON的例子中
#我們可以發現z是一個串列
#x,y,*z=a
#這條的意思是第一個和第二個分別丟到x,y中
#其餘丟到z中





#進階寫法
def f(a,b,*c):
    print(a)
    print(b)
    print(c)
#>>> f(3,7,1,4,2)
#3
#7
#(1, 4, 2)
#會發現原來函數中部只能放一個數字
#可用於資料處理





#不限定資料個數函數
def mysum(*a):
    print(a)
    return sum(a)
#>>> mysum(1,5,6,3,8)
#(1, 5, 6, 3, 8)
#23
#>>> a=[x for x in range(1,11)]
#>>> mysum(*a)
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#55

#20161223 Cycle Finding or Cycle Detection (ACM10591___Happy Number)
#將十進位數每個數字平方
#其總合為下一數字
#如果到最後可以回到1
#這個稱為快樂的數字
#例如:7--49-->97-->130-->10-->1
#若是沒辦法回來
#則稱為不快樂的數字
#例如4-->16-->37-->58-->89...-->4

#四種儲存資料
#{}-->不會紀錄重複資料
#[]-->全部紀錄
#()-->順序不可以改變
#
def ishappy(n):
    a=[]
    while n not in a:
        a.append(n)
        n = sum([int(x)**2 for x in str(n)])#整數轉字串
#三元寫法
    return 'happy' if n ==1 else'unhappy'
                
                
#普通寫法
#    if n== 1:
#        return"happy"
#    else:
#        return"unhappy"


#>>> [x for x in 123]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not iterable
#>>> [x for x in str(123)]
#['1', '2', '3']
#>>> [int(x) for x in str(123)]
#[1, 2, 3]
#>>> sum([int(x) for x in str(123)])
#6



#龜兔賽跑法(弗洛伊德演算法 Floyd's cycle-finding algorithm)
def floyd(f,x):
    y=f(x)
    while x != y :
        print('{}. {}'.format(x,y))
        x,y=f(x),f(f(y))
    return x
#把x當烏龜，y當兔子
#函數可以當參數傳遞

#>>> f=lambda x:(x**2+1)%17
#>>> floyd(f,0)
#0. 1
#1. 5
#2. 14
#5. 16
#9. 5
#14
#http://www.csie.ntnu.edu.tw/~u91029/Function.html



def ishappy2(n):
    def floyd2(f,x):
         y=f(x)
         while x != y :
             x,y=f(x),f(f(y))
         return x
    
    return floyd(lambda n:sum(int(i)**2 for i in str(n)),n)==1




#因數分解(Pollard rho)
import math
import random

def Pollard_rho(n):
    def floyd3(f,x):
        y=f(x)
        while x != y :
            m = math.gcd(abs(x-y),n)
            if m >1:
                return m
            x,y=f(x),f(f(y))
        return 1

    x0= random.randrange(n)
    return floyd3(lambda x: (x**2+1) % n, x0)
    
#f是函數
#x是初值
#n預備分解的數字
#abs絕對值

#20161223類別Vector
#連結20161216的封裝概念

#norm-->自己對自己內積
#normalize-->單位向量(向量除以長度)

#Step.1
class Vector:
    def __init__(self,*args):
        if not args:
            self.values = (0,0)
        else:
            self.values = args
#Vector是個類別
#例如 輸入a=Vector(1,2)
#而(1,2)這個向量稱為-->向量資料
#*-->可以加入很多東西
#args表示資料
#在Python中會認為
#有東西就是True
#沒東西就是False
#如果args中沒有資料(if not)
#就用(0,0)來代替
#否則逕用原有的資料

#>>> a=Vector(1,2)
#>>> b=Vector(-3,5)
#-->可以輸入資料了



#Step.4  add定義加號(building function)-->加減乘除本身沒有意義，是人定的
#Python允許改變加號的定義
    def __add__(self,other):
        return Vector(*(x+y for x,y in zip(self,other)))
#x,y從何而來?
#從a,b組合來
#透過zip指令(拉鍊，1對1，2對2......etc.)
#重新形成一個新的tuple
#*-->表示Vector的初始值
#重新定義一個新的向量
#-->定義加法的概念

#>>> a-b
#Vector(4, -3)

#>>> a+b
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "H:/WinPython/程式碼/20161223/20161223類別Vector.py", line 30, in __add__
#    return Vector(*(x+y for x,y in zip(self,other)))
#TypeError: zip argument #1 must support iteration(交互)        
#順序是人定的
#我們在輸入zip時
#並沒有提供zip順序的觀念
#-->運用zip，可以找出兩個相對應的值



#Step.6
    def __sub__(self,other):
        return Vector(*(x-y for x,y in zip(self,other)))
#概念同加法
#沒有定義負數計算
#有興趣自己去找資料

#>>> a-b
#Vector(4, -3)
#-->減法產生了



#Step.7 乘法mul(building function)
    def __mul__(self,other):
        if type(other) == type(self):
            return sum(x*y for x,y in zip(self,other))
        elif type(other) in (int,float):
            return Vector(*(other*x for x in self))

#>>> a*b(第一個乘第一個加第二個乘第二個)
#7
#>>> b*a
#7
#>>> a*3
#Vector(3, 6)
#>>> b*3
#Vector(-9, 15)
#>>> 3*a
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unsupported operand type(s) for *: 'int' and 'Vector'
#因為self在左邊，other在右邊，所以當3*a時是另一種乘法
#-->乘法產生了



#Step8.   右乘法rmul(right mul.)
    def __rmul__(self,other):
        return self*other

#>>> 3*a
#Vector(3, 6)
#>>> a*3
#Vector(3, 6)
         
            
#Step.5  iter(building function)
    def __iter__(self):
        return self.values.__iter__()
#使用tuple自身的原則(順序)
#>>> a+b
#Vector(-2, 7)
#Step.3
    def __len__(self):
        return len(self.values)
#tuple的長度就是向量的長度

#>>> len(a)
#2
#>>> len(b)
#2
#-->算出長度了



#Step.2
    def __repr__(self):
        return 'Vector' + str(self.values)
#整理資料，使輸出時為易懂的東西
      
#>>> a
#Vector(1, 2)
#>>> b
#Vector(-3, 5)
#-->現在可以抓出a,b了



#Step.9   norm算內積
    def norm(self):
        return sum(x**2 for x in self)**0.5


#Step.10   normalize單位向量
    def normalize(self):
        return 1/self.norm()*self



#>>> a=Vector(1,2)
#>>> b=Vector(-3,5)
#>>> a+b
#Vector(-2, 7)
#>>> a-b
#Vector(4, -3)
#>>> a*b
#7
#>>> 2*a+5*b
#Vector(-13, 29)
#>>> 2*a-5*b
#Vector(17, -21)

#20161230矩陣(IPython的應用)
#console是文字處理
#IPython console是圖形處理

from sympy import *
#如果是在console就醫定要打這一行
#叫出這個套件

M=Matrix(2,3,[1,-8,6,-2,4,-7])

M
#Out[60]: 
#Matrix([
#[ 1, -8,  6],
#[-2,  4, -7]])

M=Matrix([[1,0,0],[0,0,0,]]);M
#Out[61]: 
#Matrix([
#[1, 0, 0],
#[0, 0, 0]])

Matrix([[1,2,3]])
#Out[62]: Matrix([[1, 2, 3]])

Matrix([1,2,3])
#Out[63]: 
#Matrix([
#[1],
#[2],
#[3]])

M
#Out[60]: 
#Matrix([
#[ 1, -8,  6],
#[-2,  4, -7]])
eye(3)
#Out[56]: 
#Matrix([
#[1, 0, 0],
#[0, 1, 0],
#[0, 0, 1]])

ones(3)
#Out[57]: 
#Matrix([
#[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1]])

zeros(3)
#Out[58]: 
#Matrix([
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0]])

def f(i,j):
    return 1 if i == j else 0

Matrix(3,3,f)
#Out[31]: 
#Matrix([
#[1, 0, 0],
#[0, 1, 0],
#[0, 0, 1]])

Matrix(3,4,lambda i,j:1 - (i+j)%2)
#Out[32]: 
#Matrix([
#[1, 0, 1, 0],
#[0, 1, 0, 1],
#[1, 0, 1, 0]])

M=Matrix(4,4,[x for x in range(1,17)]);M
#Out[34]: 
#Matrix([
#[ 1,  2,  3,  4],
#[ 5,  6,  7,  8],
#[ 9, 10, 11, 12],
#[13, 14, 15, 16]])

M[0,3]
#Out[36]: 4

M[2,2]
#Out[37]: 11

M[0,3] = M[2,2,] = 0;M
#Out[38]: 
#Matrix([
#[ 1,  2,  3,  0],
#[ 5,  6,  7,  8],
#[ 9, 10,  0, 12],
#[13, 14, 15, 16]])

M=Matrix(4,4,[x for x in range(1,17)]);M
#Out[39]: 
#Matrix([
#[ 1,  2,  3,  4],
#[ 5,  6,  7,  8],
#[ 9, 10, 11, 12],
#[13, 14, 15, 16]])

M[0:2,1:3]
#Out[40]: 
#Matrix([
#[2, 3],
#[6, 7]])

M[1:,1:]
#Out[41]: 
#Matrix([
#[ 6,  7,  8],
#[10, 11, 12],
#[14, 15, 16]])

M[-1:,:]
#Out[42]: Matrix([[13, 14, 15, 16]])

M[:-1,:]
#Out[43]: 
#Matrix([
#[1,  2,  3,  4],
#[5,  6,  7,  8],
#[9, 10, 11, 12]])

A=Matrix(2,3,[x for x in range(1,7)]);M
#Out[44]: 
#Matrix([
#[1, 2, 3],
#[4, 5, 6]])

A=Matrix(2,2,[3,1,-1,2]);A
#Out[52]: 
#Matrix([
#[ 3, 1],
#[-1, 2]])

B=Matrix(2,2,[1,-2,3,5]);B
#Out[53]: 
#Matrix([
#[1, -2],
#[3,  5]])

A+B
#Out[54]: 
#Matrix([
#[4, -1],
#[2,  7]])

A-B
#Out[55]: 
#Matrix([
#[ 2,  3],
#[-4, -3]])

#比價
A=Matrix(2,3,[1,2,1,2,4,3]);A
#Out[73]: 
#Matrix([
#[1, 2, 1],
#[2, 4, 3]])
#A代表購買商品的個數
#有兩個矩陣，所以有兩個買法

B=Matrix(3,2,[10,15,20,18,30,25]);B
#Out[74]: 
#Matrix([
#[10, 15],
#[20, 18],
#[30, 25]])
#B代表價格

A*B
#Out[75]: 
#Matrix([
#[ 80,  76],
#[190, 177]])
#80是第一種買法在第一家商店要80元
#76是第二種買法在第二家商店要76元
#所以在第二家商店比較便宜
#190是第一種買法在第一家商店要190元
#177是第二種買法在第二家商店要177元
#所以在第二家商店比較便宜

#方陣
A = Matrix(2,2,[3,1,-1,2]);A
#Out[79]: 
#Matrix([
#[ 3, 1],
#[-1, 2]])

A**2
#Out[80]: 
#Matrix([
#[ 8, 5],
#[-5, 3]])
#即 A*A

A**50
#Out[81]: 
#Matrix([
#[-1399651561434473605432, -1273582412555111174875],
#[ 1273582412555111174875,  -126069148879362430557]])

#矩陣倒數(反矩陣)的做法
A=Matrix(2,2,[3,1,-1,2]);A
#Out[82]: 
#Matrix([
#[ 3, 1],
#[-1, 2]])

A**-1
#Out[83]: 
#Matrix([
#[2/7, -1/7],
#[1/7,  3/7]])

A.inv()
#Out[84]: 
#Matrix([
#[2/7, -1/7],
#[1/7,  3/7]])
#寫成函數寫法

#Q矩陣
#https://zh.wikipedia.org/wiki/%E6%AD%A3%E4%BA%A4%E7%9F%A9%E9%98%B5
#Q矩陣的n次方即為費氏數列
#[fn+1,fn],[fn,fn-1]
Q=Matrix([[1,1],[1,0]]);Q
#Out[86]: 
#Matrix([
#[1, 1],
#[1, 0]])

Q**10
#Out[87]: 
#Matrix([
#[89, 55],
#[55, 34]])

Q**100
#Out[88]: 
#Matrix([
#[573147844013817084101, 354224848179261915075],
#[354224848179261915075, 218922995834555169026]])

#聯立方程式
#A*X=Y
#求X
A=Matrix([[1,2],[3,4]]);A
#Out[92]: 
#Matrix([
#[1, 2],
#[3, 4]])

Y=Matrix([5,7]);Y
#Out[93]: 
#Matrix([
#[5],
#[7]])

X=A.solve(Y);X
#Out[94]: 
#Matrix([
#[-3],
#[ 4]])
#.solve-->求解之意

A*X == Y
#Out[95]: True

#產生隨機帶小數矩陣
A = Matrix(10,10,[random.randrange(20) -10.0 for _ in range(100)])
#A
#Out[102]: 
#Matrix([
#[  1,   0,  5,  9,  -5, -10,  -2,  -1,   6,  8],
#[ -1,   8, -1, -8,  -3,   2,  -6,   6,   8, -1],
#[-10,   6, -5, -5, -10,  -2,  -3, -10,   3,  8],
#[  6,  -6, -7,  3,   7,   5,   4,   5,   6, -4],
#[ -4,   0, -1,  4,   9,  -4,   7,  -6,  -6, -9],
#[  4, -10,  6,  3,  -1,   5,  -2,  -4,   3,  5],
#[  8,   4,  6,  5,   2,   4,   7,  -6, -10, -9],
#[ -3,   8, -8, -8,  -3,   9,   7,   0,  -3, -7],
#[  6,  -1,  0,  9,   8,   5,  -5,   0,  -7,  7],
#[ -4,   7,  1, -1,   2,   9, -10,  -3,   1, -4]])
#若不帶小數
#就把10.0改10

#製圖
import math
import random

from pylab import *
x = linspace(-5,3,1000)
plot(x,(x+4)*(x+1)*(x-2))
grid(True)
axhline(linewidth=2, color='k')
axvline(linewidth=2, color='k')
#Out[122]: <matplotlib.lines.Line2D at 0xb4d9cc0>
￼#產生圖片
#b代表blue
#c代表藍綠色
#k代表black
#from pylab import *-->叫出一個套件
#http://matplotlib.org/
#pylib是和matplotlib相同類型的小工具可以參考一下
#APP Maker
#linspace線性資料
#從-5到3
#產生1000個座標點
#y座標就是後面的方程式
#grid對其用的小格限
#axhline-->X軸
#axvline-->Y軸
#linewidth-->線寬

#二分法求根圖
from pylab import *
f = lambda x : x**2 - 3*x + 2
x = linspace(-0.2,2.5,1000)
plot(x,f(x))
grid(True)
axhline(linewidth=2,color='k')

x1 = 0
plot((x1,x1), (0, f(x1)),'r')
x2 = 1.5
plot((x2,x2), (0, f(x2)),'r')

x = (x1+x2)/2
plot((x,x), (0, f(x)), 'r')

x = (x1 ,x, x2)
labels = ('x1',r'x = (x1+x2)/2', 'x2')
xticks(x,labels)
#Out[159]: 
#([<matplotlib.axis.XTick at 0xd0fff28>,
#  <matplotlib.axis.XTick at 0xb2a8780>,
#  <matplotlib.axis.XTick at 0xd174208>],
# <a list of 3 Text xticklabel objects>)
#圖形
#plot-->畫出來的意思
#x1-->兩個x座標根兩個y座標
#所以其實是(x1,0)根(x1,f(x1))的兩點
#labels是指標籤
#最後xticks是指說把他畫出來

#https://www.google.com.tw/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=sympy%20calculus
#微積分的應用(上面是網站，下面是範例)
#eg.1
#>>> from sympy import*
#>>> x = symbols('x')
#>>> diff(cos(x),x)
#-sin(x)
#eg.2
#>>> diff(sin(tan(x)+cos(x)),x)
#(-sin(x) + tan(x)**2 + 1)*cos(cos(x) + tan(x))

#sin,cos的圖形
from pylab import *
figure(figsize = (10, 6))
x1 , x2 = 0, 2
x = linspace(x1 ,x2, 500)
y1, y2 = sin(2*pi*x),cos(2*pi*x)
plot(x, y1, 'b', label = 'sin')
plot(x, y2, 'r', label = 'cos')

xgap, ygap = 0.05, 0.1
xlim(x1 - xgap, x2 + xgap)
ylim(-1 - ygap, 1.3 + ygap)
legend(loc = 'upper right')
xlabel('x')
ylabel('y')
grid(True)
#figure設定大小
#lim設定邊界

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.plot()
#numpy數字型的套件
#np本身有自己的random number
#alpha表示透明度

##20170106
#insert(插入資料)
#>>> a=[8,2,7,0,6]
#>>> a.insert(1,9)
#>>> a
#[8, 9, 2, 7, 0, 6]

#index(尋找位置)
#>>> i=a.index(0)
#>>> a.insert(i,-1)
#>>> a
#[8, 9, 2, 7, -1, 0, 6]
#尋找出0的位置，並在0的位置插入-1

#pop找出指定位置的資料並移除
#>>> a.pop(1)
#9
#>>> a
#[8, 2, 7, -1, 0, 6]
#pop是利用資料的位置以移除

# remove(移除)
#>>> a.remove(-1)
#>>> a
#[8, 2, 7, 0, 6]
#remove是利用資料本身以移除

#using lists and stacks(將資料視為盤子，取資料時自最高處取用，此為堆疊)
#push(將資料放上去)
#pop(將資料取出)
#>>> stack=[1,2,3,4,5]
#>>> 
#>>> stack.append(6)
#>>> stack.append(7)
#>>> stack
#[1, 2, 3, 4, 5, 6, 7]
#>>> 
#>>> stack.pop()
#7
#>>> stack
#[1, 2, 3, 4, 5, 6]
#>>> 
#>>> stack.pop(-1)
#6
#>>> stack
#[1, 2, 3, 4, 5]
#想取出最後一筆資料，除了可以使用最後一筆資料的位置外
#亦可忽略不寫
#也可以利用-1
#last-in first-out priciple (LIFO 後進先出)
#函數的呼叫便是堆疊的應用(副程式的呼叫，尤其連CPU都使用硬體的堆疊)

#Using Lists as Queues(排隊 / 佇列)
#first-in first-out principle (FIFO 先進先出)
#資料不夠，增開更大的空間將資料騰過去
#缺點是所有資料的排序會受到影響
#because all of the other elements have to be shifted by one
#沒有效率(移動一個，所有資料都會左移或右移)
#>>> from collections import deque
#de表示雙向關係
#>>> queue = deque([1,2,3,4,5])
#>>> 
#>>> queue.append(6)
#>>> queue.append(7)
#>>> queue
#deque([1, 2, 3, 4, 5, 6, 7])
#>>> 
#>>> queue.appendleft(6)
#>>> queue.appendleft(7)
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])

#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])
#>>>  
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])
#>>> queue.pop()
#7
#>>> queue.pop()
#6
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5])
#>>> queue.popleft()
#7
#>>> queue.popleft()
#6
#>>> queue
#deque([1, 2, 3, 4, 5])

#Using Heaps(資料結構的一種，適合實作Priority Queue，二元素作法) as Priority Queues(具優先次序的佇列(根據優先權決定順序)，簡單說就是插隊)
#How to use Heaps as Priority Queues?
#>>> import heapq as pq
#>>> h = [6,5,1,2,0]
#>>> pq.heapify(h)
#>>> h
#[0, 2, 1, 6, 5]
#>>> 
#>>> pq.heappush(h,9)
#>>> pq.heappush(h,7)
#>>> h
#[0, 2, 1, 6, 5, 9, 7]
#>>> 
#>>> pq.heappop(h)
#0
#>>> pq.heappop(h)
#1
#>>> h
#[2, 5, 7, 6, 9]

#堆積排序法(Heapsort)
import heapq as pq
def heapsort(a):
    h=[]
    for x in a:
        pq.heappush(h,x)
        
    return [pq.heappop(h) for _ in range(len(h))]

#>>> import random
#>>> a=random.sample(range(100),20)
#>>> a
#[83, 79, 28, 18, 55, 92, 61, 69, 19, 71, 95, 97, 34, 37, 94, 1, 81, 88, 90, 20]
#>>> 
#>>> heapsort(a)
#[1, 18, 19, 20, 28, 34, 37, 55, 61, 69, 71, 79, 81, 83, 88, 90, 92, 94, 95, 97]

#RSA公開金鑰系統
#Fermat's little theorem states that if p is prime and 1<a<p,then
#a**(p-1)等意於1  (mod p)
#>>> n=221
#>>> a=38
#>>> pow(a,n-1,n)
#1
#221 may be a prime number
#>>> a=24
#>>> pow(a,n-1,n)
#81
#221 is not a prime number

import random

def isprime(n, k = 128):
    if n<2:
        return False
        
    for _ in range(k):
        a = random.randrange(1,n)
        if pow(a, n-1, n) != 1:
            return False
    return True
    
#>>> n=2**127-1
#>>> isprime(n)
#True
#>>> n=2**127+1
#>>> isprime(n)
#False

def nextprime(n, k =128):
    if n<2:
        return 2
    
    n+=1
    while not isprime(n,k):
        n+=1
        
    return n
    
#>>> p=nextprime(random.randrange(10**200))
#>>> p
#62756299807539435861740661436024023267371433179232367639969413409427936012915825334535413998498960592008203871528363988102475873837917758232308608226471309111359149757800103786306450678970693972566073

#Hash Function
#>>> import hashlib
#>>> password='123456'
#>>> 
#>>> h=hashlib.md5()
#>>> h.update(password.encode())
#>>> h.hexdigest()
#'e10adc3949ba59abbe56e057f20f883e'
#>>> h.digest_size, 8*h.digest_size
#(16, 128)
#>>> 
#>>> h=hashlib.sha256()
#>>> h.update(password.encode())
#>>> h.hexdigest()
#'8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'
#>>> h.digest_size, 8*h.digest_size
#(32, 256)

#Salt(cryptography)
#密碼是儲存hash code而不是字串
#>>> dk = hashlib.pbkdf2_hmac('sha256',b'password',b'salt',10000)
#>>> dk.hex()
#'0394a2ede332c9a13eb82e9b24631604c31df978b4e2f0fbd2c549944f9d79a5'
#sha256是只有265位元
#b'password'是密碼
#反覆做100,000次