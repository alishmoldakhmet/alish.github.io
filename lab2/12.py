a=[1,2,2,3,5]
for i in range(len(a)):
    for j in range(0,i):
        if a[j]==a[i]:
            a[i]=a[j]**2
print(a)
