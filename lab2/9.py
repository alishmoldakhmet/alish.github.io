a=(1,2,3,[1,2,3],5)
for i in range(len(a)):
    if type(a[i])==list:
        print(True)
        exit()
print(False)