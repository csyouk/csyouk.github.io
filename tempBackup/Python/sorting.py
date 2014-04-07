a=[7,1,2,33,7,9,9,5,3,12]


def mysort(list):
	for index1 in xrange(0,len(list)):
		for index2 in xrange(0,len(list)):
			if a[index1] <= a[index2]:
				print 'pass'
			else:
				temp1 = a[index1]
				print temp1
				temp2 = a[index2]
				print temp2
				a[index1] = temp1
				print 'a[index1] is ', a[index1]
				a[index2] = temp2
				print 'a[index2] is ', a[index2]				
	return list			

print mysort(a)	