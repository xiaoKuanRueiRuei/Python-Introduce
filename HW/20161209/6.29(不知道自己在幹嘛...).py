def isValid(number):
    a=0
    while number != 0:
        b = number % 100 // 10
        if b >= 5:
            b = (2*b) % 10 + (2*b) // 10
        else:
            b=b
            a = a+2*b
        number = number // 100
    return a
    
def sumOfDouble(number):
    a=0
    while number != 0:
        b = number % 10
        if b >= 5:
            b = (2*b) % 10 + (2*b) // 10
        else:
            b=b
            a = a+2*b
        number = number // 100
    return a
    
def getDigit(number):
    isValid(number)+sumOfDouble(number)
    
def sumOfOddPlace(number):
    return isValid(number)
    
def prefixMatched(number,d):
    if getDigit(number)%10==0:
        return true
    else:
        return false  
        
def getSized(d):
    
def getPrefix(number,k):
