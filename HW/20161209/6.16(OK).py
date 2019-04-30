def numberOfYear(year):
    if year %4 != 0:
        result="365days"
    elif year %100 == 0:
        result="365days"
    else:
        result="366days"
    print(year,result,end=" ")
    
for year in range(2010,2021,1):
    if year>0:
        result1=numberOfYear(year)
    else:
        result2=""
    print()
