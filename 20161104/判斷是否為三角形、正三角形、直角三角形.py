def g(a,b,c):
	if a+b<=c:
		result="非三角形"
	elif b+c<=a:
		result="非三角形"
	elif a+c<=b:
		result="非三角形"
	elif a**2+b**2==c**2:
		result="直角三角形"
	elif a**2+c**2==b**2:
		result="直角三角形"
	elif b**2+c**2==a**2:
		result="直角三角形"
	elif a==b==c:
		result="正三角形"
	else:
		result="非直角與正三角形之三角形"
	print(result)