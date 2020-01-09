def f(x):
    return pow(x-4,2)+pow(x,4)

def thirds(a,b,tolerance=1e-2):
    while(abs(a-b)>tolerance):
        step=abs(a-b)/3
        c=a+step
        d=c+step
        if(f(c)>f(d)):
            a=c
        else:
            b=d
    return [a,b]
import math
#Golden Number
gn = (math.sqrt(5) + 1) / 2 

def golden_method(a,b,tolerance=1e-2):
    while(abs(a-b)>tolerance):
        #We calculate C we the Golden Number but we can alo calculate with the golden ratio like this:
        c = b - (b - a) /gn
        d = a + (b - a) / gn
        if(f(c)>f(d)):
            a=c
        else:
            b=d
    return [a,b]

def uni_search(a,b):
    h=(a+b)/20
    c=a
    d=a
    for i in range(0,30):
        if(f(a)>f(c)):
            a=d
            d=c
            h=h/2
        else:
            d=c
            c=a
            if((a+h)<b):
                a=a+h
            else:
                a=b
    return [a,(a+b)/2,b]

def quadratic_interpolation(a,c,b):
    h=(b-a)/2
    return a-(h*(f(a)-f(b)))/(2*(f(a)-2*f(c)+f(b)))

def find_min_thirds(a,b):
    l1=thirds(0,2)
    l2=uni_search(l1[0],l1[1])
    return quadratic_interpolation(l2[0],l2[1],l2[2])

def find_min_golden(a,b):
    l1=thirds(0,2)
    l2=uni_search(l1[0],l1[1])
    return quadratic_interpolation(l2[0],l2[1],l2[2])


print(find_min_thirds(1,1.2))

print(find_min_golden(1,1.2))