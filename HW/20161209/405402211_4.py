#6.2
def sumDigits(x):
    a=0
    while x != 0:
        a = a+x % 10
        x = x // 10
    print(a)
    
#6.3
def reverse(number):
    b=0
    while number != 0:
            b=b*10+number%10
            number=number//10
    return b

def isPalindrome(number):  
    if number == reverse(number):
        print(number,"is a palindrome integer.")
    else:
        print(number,"is not a palindrome integer.")
        
#6.8
#Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    Fahrenheit = round( (9/5)*celsius + 32,1)
    return Fahrenheit

#Converts from Fahrenheit to Celsius
def FahrenheitTocelsius(Fahrenheit):
    celsius =round( ((5/9)*(Fahrenheit - 32)),2)
    return celsius


print("Celsius     Fahrenheit   |   Fahrenheit     Celsius")
a=[x for x in range(40,30,-1)]
b=[y for y in range(120,20,-10)]
for i,q in zip(a,b):
    t=celsiusToFahrenheit(i)
    b=FahrenheitTocelsius(q)
    print('%2.1f '%i ,' ','%10.1f'%t,'      |       ','%5.1f'%q,'%10.2f'%b)

#6.10
def isPrime(number):
    divisor = 2
    while divisor <= number / 2 :
        if number % divisor == 0:
            return False
        divisor+=1

    return True
    
def prime():
    a=[]
    for x in range(1,10000):
        if isPrime(x) is True:
            a.append((x))
    print(len(a))
prime()

#6.16
def numberOfYear(year):
    if year %4 != 0:
        result="365days"
    elif year %100 == 0:
        result="365days"
    else:
        result="366days"
    print(year,result,end=" ")
    
for year in range(2010,2021,1):
    if year>0:
        result1=numberOfYear(year)
    else:
        result2=""
    print()

#6.29
