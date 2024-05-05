from math import sqrt

a=2 
b=1
c=2

q = (b**2) - (4*a*c)

if q < 0:
     print("No real solutions")
else:
    q_sr = sqrt(q)
    x1 = (-b + q_sr)/2*a
    x2 = (-b - q_sr)/2*a
    print(x1,x2)





