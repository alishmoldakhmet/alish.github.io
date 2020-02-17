def asd(a,b):
    for i in range(b,len(a)):
        a[i]=a[i]**2
    return a
a=[1,2,3,4,5]
b=int(input())
print(asd(a,b))