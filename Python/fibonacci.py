def fibonacci(n):
	if n<2:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))

for terms in range(0,7):
	print fibonacci(terms)