a,b,c=[float(x) for x in input("Enter a,b,c :").split(",")]
d=b **2  - 4 * a * c
e=(-b-(b**2-4*a*c)**0.5)/2*a
f=(-b+(b**2-4*a*c)**0.5)/2*a
if d < 0 :
    print("The equation has no real roots.")
elif d==0 :
    print("The root is " , float(-b/2*a))
else:
    print("The roots are %.5f" %(e),"and %.5f" %(f))
    
 
    

    
a,b,c,d,e,f=[float(x) for x in input("Enter a,b,c,d,e,f:").split(",")]
g= a * d - b * c
if g == 0:
    print("The equation has no solution.")
else:
    print( "x is ",( e * d - b * f) / g , 1 , "and y is ", (a * f - e * c ) / g )

    
    
    
    
a=float(input('Enter weight in pounds:'))
b=float(input('Enter feet:'))
c=float(input('Enter inches:'))
d=a*0.45359327
e=(b*12+c)*0.0254 
bmi= d/e**2
print("BMI is " , format(bmi) )
if bmi < 18.5 :
    print("You are Underweight.")
elif bmi < 25 :
    print("You are Normal.")
elif bmi < 30 :
    print("You are Overweight.")
else :
    print("You are Obese.")

    
    
    
    
a,b,c=[float(x) for x in input("請鍵入三個數字:").split(",")]
d=[a,b,c]
print(sorted(d))





a,b=[float(x) for x in input("Enter weight and price for package:").split(",")]
c,d=[float(x) for x in input("Enter weight and price for package:").split(",")]
if b/a > d/c :
    result="Package 1 has the better price."
elif b/a < d/c :
    result="Package 2 has the better price."
else:
    result="The price of Package 1 and the price of Package 2 have the same price."
print(result)





a=int(input("Enter an integer:"))
if a%6==0 and a%5==0:
    print("Is",a,"divisible by 5 and 6? Ture.")
    print("Is",a,"divisible by 5 or 6? Ture.")
    print("Is",a,"divisible by 5 or 6 , but not both? False.")
elif a%6 == 0 and a%5 > 0:
    print("Is",a,"divisible by 5 and 6? False.")
    print("Is",a,"divisible by 5 or 6? Ture.")
    print("Is",a,"divisible by 5 or 6 , but not both? Ture.")
elif a%6 > 0 and a%5 == 0 :
    print("Is",a,"divisible by 5 and 6? False.")
    print("Is",a,"divisible by 5 or 6? Ture.")
    print("Is",a,"divisible by 5 or 6 , but not both? Ture.")
else:
    print("Is",a,"divisible by 5 and 6? False.")
    print("Is",a,"divisible by 5 or 6? False.")
    print("Is",a,"divisible by 5 or 6 , but not both? False.")
    
    
    
    
    
y=int(input("Enter year:(e.g.,2008):"))
m=int(input("Enter month:1-12:"))
q=int(input("Enter the day of the month:1-31:"))
k=y%100
j=y//100 
a=k//4
c=(k-1)//4
b=j//4
if m<2:
    h=( q + 26*(m+13)//10 + k-1 + c + b + 5*j ) % 7
else:
    h =( q + 26*(m+1)//10 + k + a + b + 5*j ) % 7
f =(h%7+7)%7
if h == 0 or f == 0:
    print("Day of week is Saturday")
elif h == 1 or f == 1:
    print("Day of week is Sunday")
elif h == 2 or f == 2:
    print("Day of week is Monday")
elif h == 3 or f == 3:
    print("Day of week is Tuesday")
elif h == 4 or f == 4:
    print("Day of week is Wednesday")
elif h == 5 or f == 5:
    print("Day of week is Thursday")
else:
    print("Day of week is Friday")