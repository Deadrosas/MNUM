import math as m
k=2.5
h1=0.125
h2=0.0625
h3=0.03125

def df(x):
    return m.sqrt(1+pow(k*m.exp(k*x),2))


def trapezium(a,b,h):
    n=round(abs(b-a)/h)
    sum=df(a)+df(b)
    for i in range(1,n):
        sum+=2*df(a+i*h)
    return sum*h/2

print(trapezium(0,1,h1))
print(trapezium(0,1,h2))
print(trapezium(0,1,h3))