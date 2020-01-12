import math as m
def f(x):
    return m.sqrt(1+pow(2.5*m.exp(2.5*x),2))

def trapezium(a,b,h):
    sum=f(a)+f(b)
    n=round(abs(b-a)/h)
    for i in range(1,n):
        sum+=2*f((a+i*h))
    
    return float(sum*h/2)


def simpson(a,b,h):
    sum=(f(a)+f(b))
    n=round(abs(b-a)/h)
    for i in range(1,n):
        if(i%2==0):
            sum+=2*f(a+i*h)
        else:
            sum+=4*f(a+i*h)
    return float(sum*(h/3))


print("Area underneath the curve for h=0.125: ",trapezium(0,1,0.125))
print("Area underneath the curve for h=0.0625: ",trapezium(0,1,0.0625))
print("Area underneath the curve for h=0.03125: ",trapezium(0,1,0.03125))
print("Error for trapezium:",(trapezium(0,1,0.03125)-trapezium(0,1,0.0625))/3)


print("Area underneath the curve for h=0.125: ",simpson(0,1,0.125))
print("Area underneath the curve for h=0.0625: ",simpson(0,1,0.0625))
print("Area underneath the curve for h=0.03125: ",simpson(0,1,0.03125))
print("Error for Simpson:",(simpson(0,1,0.03125)-simpson(0,1,0.0625))/15)