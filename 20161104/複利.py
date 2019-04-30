P=1000000
r=5/100/12
t=20*12
F=P*(1+r)**t

def ci (P,r,t):
     return P*(1+r/12)**(t*12)