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
