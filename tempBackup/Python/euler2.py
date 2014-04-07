Fibbonacci = [0,1]
evenFibbonacci =[]

"""
j=0
Fibbonacci[j]
print Fibbonacci[j]
Fibbonacci[j+1]
print Fibbonacci[j+1]


sum= Fibbonacci[j] + Fibbonacci[j+1]
print sum
Fibbonacci.append(sum)
print Fibbonacci
"""

"""
	for i in range(0,20):
		if i > 10 :
			break
		print i	
"""

for i in range(0,1000):
	term_n1 = Fibbonacci[i]
	term_n2 = Fibbonacci[i+1]
	limit = 4000000
	sum = term_n1 + term_n2
	Fibbonacci.append(sum)
	if sum%2==0:
		evenFibbonacci.append(sum)
		#print evenFibbonacci
	if sum > limit:
		break	
	#print Fibbonacci

"""
print evenFibbonacci
print Fibbonacci
"""
print evenFibbonacci

sum2=0
for j in range(0,len(evenFibbonacci)):
	sum2 = sum2 + evenFibbonacci[j]
	print sum2
