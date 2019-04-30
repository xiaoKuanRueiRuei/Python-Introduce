a,b=[float(x) for x in input("Enter weight and price for package:").split(",")]
c,d=[float(x) for x in input("Enter weight and price for package:").split(",")]
if b/a > d/c :
    result="Package 1 is the better price."
elif b/a < d/c :
    result="Package 2 is the better price."
else:
    result="The price of Package 1 and the price of Package 2 are the same."
print(result)