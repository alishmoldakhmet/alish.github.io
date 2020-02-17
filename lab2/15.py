import math
def rec(n):
    x=[]
    y=[]
    x[0]=4
    y[0]=2
    e=int(0,5/n)+1
    for i in range(1,e):
     x[i]=2+(n*(i-1))
     y[i]=y[i-1]+n*(0,1*((y[i-1])**(1/2))+0,4*((x[i-1]*2)))
     return x[i],y[i]
h=float(input())
print(rec(h))    

