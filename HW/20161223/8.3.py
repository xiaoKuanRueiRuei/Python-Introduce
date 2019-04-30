def password(a):
    for c in a:
        if (c.isdigist()):
            count+=1
    return all([
        count>=2,
        any(c in ["!","@","#","$",","]),
        len(a)>=8])
        
    
    