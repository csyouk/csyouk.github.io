def median(list):
    a=sorted(list)
    b=len(a)
    #print b
    if b%2==1:
    	M=a[b/2]
    	#print M
    	return M
    else:
    	M1 = int(b/2.0)
    	M2 = int((b/2.0)-1)
    	#print M1, M2
    	M= (a[M1]+a[M2])/2.0
    	return M
    	
print median([4,5,5,4])