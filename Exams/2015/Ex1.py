def df(T,t):
    return -0.25*(T-37)

def Euler(T,t,step):
    for i in range(2):
        T=T+df(T,t)*step
        t=t+step
    
    return T

print(Euler(3,5,0.4))