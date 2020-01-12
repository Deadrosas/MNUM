import math as m
def f(x):
    return pow(x,3)-10*m.sin(x)+2.8

def bissection(a,b,function):
    for i in range(2):
        m=(a+b)/2
        if(function(m)*function(a)<0):
            b=m
        else:
            a=m
    print("O valor da raíz esta entre {} e {}".format(a,b))

bissection(1.5,4.2,f)
