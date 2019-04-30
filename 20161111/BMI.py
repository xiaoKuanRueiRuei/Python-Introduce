a=float(input('體重:'))
b=float(input('身高:'))
c=a/(b*0.01)**2
if c < 18.5:status="體重過輕"
elif c<24:status="正常範圍"
elif c < 27:status="體重過重"
elif c <30:status="輕度肥胖"
elif c <34:status="中度肥胖"
elif c >=34: status="重度肥胖"
print(status)