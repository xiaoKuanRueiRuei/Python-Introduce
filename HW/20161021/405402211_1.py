a=float(input('Enter a degree in Celsius:'))
print ( a , 'Celsius is ' , a * 1.8 + 32 , 'Fahrenheit' )





import math
a,b= [float(x) for x in input('Enter the radius:' 'length of a Cylinder:').split(',')]
c=a**2*math.pi
d=a**2*3.14*b
print('The area is %.4f'%(c),'and the volume is %.4f'%(d) )







a=float(input('Enter a value for feet:'))
print(a, 'feet is ' ,a*0.305 ,'meters')








a=float(input('Enter a value for pounds:'))
print(a, 'pounds is ' ,a*0.454 ,'kilograms')








a,b=[float(x) for x in input('Enter the subtotal:' 'Enter a gratuity rate:').split(',')]
print('The gratuty is',a*b*0.01,'and the total is',a+a*b*0.01)







a=float(input('Enter final account value:'))
b=float(input('Enter annual interest rate in percent:'))
c=float(input('Enter number of years:'))
print('Initial deposit value is',a/(1+b/1200)**(c*12))






a=0
b=1
n=5
for i in range(1,n+1):
    a+=1
    b+=1
    print(a,b,a**b)