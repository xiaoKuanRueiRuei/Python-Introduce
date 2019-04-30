#8.3
def checkpassword(a):
    count=0     
    for c in a:
        if (c.isdigit()):
            count +=1
    if count>=2:
        if not any(c in ['!','@','#','$',','] for c in a):
            if all([any(c.isalpha() for c in a),any(c.isdigit() for c in a),len(a)>=8]):
                print('valid password')
            else:
                print('invalid password')
        else:
            print('invalid password')
    else:
        print('invalid password')

#8.5
def count(s1,s2):
   print(str(a).count(str(b)))
a=str(input('Enter Number A:'))
b=str(input('Enter Number B:'))
count(a,b)

#8.8
def binaryToDecimal(binaryString):
    a=0
    n=0
    while binaryString != 0:
        a = a + ((binaryString % 10)*(2**n))
        binaryString = binaryString // 10
        n+=1
    print(a)

#8.10
def decimalToBinary(value):
    a=0
    i=0
    while value != 0:
        a = a + value % 2 * 10**i
        value = value // 2
        i+=1
    print(a)

#8.12
        

#8.15
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