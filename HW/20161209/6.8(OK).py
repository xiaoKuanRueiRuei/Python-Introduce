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