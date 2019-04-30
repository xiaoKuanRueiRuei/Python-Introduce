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