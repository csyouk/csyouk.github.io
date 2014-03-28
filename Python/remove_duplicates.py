def remove_duplicates(x):
    a=[]
    for i in range(len(x)):
        if x[i] not in a:
            a.append(x[i])
    return a
    
print remove_duplicates([1,2,3,3])    