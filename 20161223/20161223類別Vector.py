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