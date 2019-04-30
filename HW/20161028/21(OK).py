y=int(input("Enter year:(e.g.,2008):"))
m=int(input("Enter month:1-12:"))
q=int(input("Enter the day of the month:1-31:"))
k=y%100
j=y//100 
a=k//4
c=(k-1)//4
b=j//4
if m<2:
    h=( q + 26*(m+13)//10 + k-1 + c + b + 5*j ) % 7
else:
    h =( q + 26*(m+1)//10 + k + a + b + 5*j ) % 7
f =(h%7+7)%7
if h == 0 or f == 0:
    print("Day of week is Saturday")
elif h == 1 or f == 1:
    print("Day of week is Sunday")
elif h == 2 or f == 2:
    print("Day of week is Monday")
elif h == 3 or f == 3:
    print("Day of week is Tuesday")
elif h == 4 or f == 4:
    print("Day of week is Wednesday")
elif h == 5 or f == 5:
    print("Day of week is Thursday")
else:
    print("Day of week is Friday")