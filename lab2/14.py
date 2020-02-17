import math
def min(a,b):
    d=((((a+b)+(((a-b)**2)**(1/2)))//2)-((a-b)**2)**(1/2))
    return int(d)
a=int(input())  
b=int(input()) 
c=int(input()) 
d=int(input())   
e=min(a,b)
f=min(c,d)
print(min(e,f))

