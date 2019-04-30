a=float(input('Enter final account value:'))
b=float(input('Enter annual interest rate in percent:'))
c=float(input('Enter number of years:'))
print('Initial deposit value is',a/(1+b/1200)**(c*12))