def roots(a = 2,b = -3,c = 1):
     d = b**2 - 4*a*c
     r1 = (-b + d**0.5)/(2*a)
     r2 = (-b - d**0.5)/(2*a)
     if d > 0:
         print('實根')
     elif d < 0:
         print('虛根')
     else:
         print('重根')
     print('r1 =',r1)
     print('r2 =',r2)
