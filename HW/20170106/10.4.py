a=[int(x) for x in input("請輸入成績:").split()]

average = sum(a) / len(a)
print("平均:",average,"分")

b=0
c=0

for x in range (0,len(a)):
    if a[x] >= average:
        b+=1
    else:
        c+=1
        
print("有",b,"人高於平均")
print("有",c,"人低於平均")