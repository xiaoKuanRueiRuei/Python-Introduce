def gcd1(a,b):
    for i in range (1,min(a,b)+1):
        if(a%i==0) and (b%i==0):
            x=i
    return x
#千萬不要用


def gcd2(a,b):
    while b>0:
        a,b=b,a%b
    return a
#輾轉相除法


def gcd3(a,b):
    if b==0:
        return a
    
    return gcd3(b,a%b)
#遞迴(自己呼叫自己)
    

def gcd4(a,b):
    return a if b == 0 else gcd4(b,a%b)
#遞回，三元寫法