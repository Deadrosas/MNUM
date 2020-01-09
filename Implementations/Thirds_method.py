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

print(thirds(0,4))