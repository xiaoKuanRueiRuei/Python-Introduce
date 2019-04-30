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