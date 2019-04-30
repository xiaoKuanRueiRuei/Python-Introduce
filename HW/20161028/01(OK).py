a,b,c=[float(x) for x in input("Enter a,b,c :").split(",")]
d=b **2  - 4 * a * c
e=(-b-(b**2-4*a*c)**0.5)/2*a
f=(-b+(b**2-4*a*c)**0.5)/2*a
if d < 0 :
    print("The equation has no real roots.")
elif d==0 :
    print("The root is " , float(-b/2*a))
else:
    print("The roots are %.5f" %(e),"and %.5f" %(f))

        
        
