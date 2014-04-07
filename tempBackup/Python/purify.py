def purify(li):
    L=[]
    for index in range(len(li)):
        if li[index]%2==0:
            L.append(li[index])
    return L

print purify([0,1,2,13,11,12])