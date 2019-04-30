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