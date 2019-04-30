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