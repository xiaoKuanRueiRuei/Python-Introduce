def g(a,b,c):
	if a+b<=c:
		result="false"
	elif b+c<=a:
		result="false"
	elif a+c<=b:
		result="false"
	else:
		result="Ture"
	print(result)