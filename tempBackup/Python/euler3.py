def isPrime(x):
    factor = []
    half = int(round(x/2))
    for i in range(1,half):
    	if x%i==0:
    		factor.append(i)
    print factor
    

#isPrime(60000003)    		


import math
def isPrime(num):
	r = 2
	while(r<num):
			if(num % r ==0):
				return False
			r += 1
	return True
 
def isNumber(x):
	n = int(x)
	if n == x:
		return True
	return False
 
 
 
found = []
def temp(num):
	s = 1
	while(s <= num):
		s += 1
		if (num % s == 0):
			if isPrime(s):
				print "%d is Prime" % s
				found.append(s)
			a = num / s
			if a < s : 
				return a
			loop = True
			while(isNumber(a)):
				print "inspect: %d" % a
				if isPrime(a):
					print "%d is Prime" % a
					found.append(a)
				a = math.sqrt(a)
			print "end counter inspect"
 
temp(600851475143)
print sorted(found)[-1]