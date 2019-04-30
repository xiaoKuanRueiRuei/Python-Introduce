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