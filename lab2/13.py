a=[1,2,3,4,2,1]
b=[]
cnt=0
for i in range (0,len(a)):
   b.append(a.count(a[i])) 
print(b)
for i in range(0,len(a)):
    if b[i]%2==1:
        cnt+=1
        
if cnt>1:
    print("No")
else:
    print("Yes")