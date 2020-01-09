def func(x):
    return pow(x,4)+2*pow(x,3)-x-1


def bissection(a,b,function,precision):
    for i in range(0,precision):
        m=(a+b)/2
        if(function(m)*function(a)<0):
            b=m
        else:
            a=m
    print("O valor da raíz esta entre {} e {}".format(a,b))
    return m

print("Result: ",bissection(0,5,func,50))