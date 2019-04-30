# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:36:33 2016

@author: user
"""

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
        
            
                   
    
def binarytodecimal():
    binary = input('enter a binary number: ')
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print (decimal)
binarytodecimal()
    
def decimaltobinary(value):
    if value > 1:
       decimaltobinary(value//2)
    print(value % 2,end='')
value = int(input("Enter a decimal number: "))
decimaltobinary(value)


def ISBN():
    ISBN=(str(input('Please enter the 9 digit number: ')))
    Digit1=int(ISBN[0])*1
    Digit2=int(ISBN[1])*2
    Digit3=int(ISBN[2])*3
    Digit4=int(ISBN[3])*4
    Digit5=int(ISBN[4])*5
    Digit6=int(ISBN[5])*6
    Digit7=int(ISBN[6])*7
    Digit8=int(ISBN[7])*8
    Digit9=int(ISBN[8])*9
    Sum=(Digit1+Digit2+Digit3+Digit4+Digit5+Digit6+Digit7+Digit8+Digit9)
    Digit10=Sum%11
    if Digit10==10:
        Digit10='X'
        ISBNNumber=str(ISBN)+str(Digit10)
    print(ISBNNumber)
ISBN()

    