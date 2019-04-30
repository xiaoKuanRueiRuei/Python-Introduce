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


