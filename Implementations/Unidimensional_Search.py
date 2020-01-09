from math import cos
def func(x):
    return pow(x-4,2)+pow(x,4)


def uni_search(a,b):
    h=(a+b)/20
    c=a
    d=a
    for i in range(0,30):
        if(func(a)>func(c)):
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
    return a

print(uni_search(0,5))
