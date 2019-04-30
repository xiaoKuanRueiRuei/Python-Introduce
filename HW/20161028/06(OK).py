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
