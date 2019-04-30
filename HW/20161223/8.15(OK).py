a=int(str(input('Enter the first 9 digits of an ISBN-10 as a string:')))
b=a%10*9
c=a//10
z=c%10*8
d=c//10
y=d%10*7
e=d//10
x=e%10*6
f=e//10
w=f%10*5
g=f//10
v=g%10*4
h=g//10
u=h%10*3
i=h//10
t=i%10*2
j=i//10
s=j%10*1
aa=(b+z+y+x+w+v+u+t+s)%11
if aa!=10:
    print("The ISBN-10 number is ",end="")
    print(a,end="")
    print(aa)
else:
    print("The ISBN-10 number is ",end="")
    print(a,end="")
    print("X")