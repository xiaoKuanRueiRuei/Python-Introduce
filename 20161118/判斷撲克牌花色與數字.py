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