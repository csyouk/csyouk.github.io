def euler1(x):
    sum=0
    for i in range(1,x):
        if i%3==0 or i%5==0:
            sum = sum + i
    print sum        

euler1(1000)


def euler1other(y):
    A=[]
    B=[]
    for i in range(1,y):
        if i%3==0:
            A.append(i)
        elif i%5==0:
            A.append(i)
        else:
            B.append(i)
    sum = 0        
    for j in range(0,len(A)):
        sum = sum + A[j]
        print sum

euler1other(1000)            
