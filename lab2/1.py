def IsPointInSquare(x, y):
    return z+r>=x>=z-r and d+r>=y>=d-r and ((((x-z)**2)+((y-d)**2))**(1/2))<=r
x=float(input())   
y=float(input())
z=float(input())   
d=float(input())
r=float(input())   
if (IsPointInSquare(x,y)):
    print("YES")
else:
    print("NO")    