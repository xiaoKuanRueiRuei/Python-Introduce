a,b,c,d,e,f=[float(x) for x in input("Enter a,b,c,d,e,f:").split(",")]
g= a * d - b * c
if g == 0:
    print("The equation has no solution.")
else:
    print( "x is ",( e * d - b * f) / g , 1 , "and y is ", (a * f - e * c ) / g )