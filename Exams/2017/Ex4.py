import math as m
def fc(c,t):
    return -1*m.exp(-0.5/(t+273))*c

def ft(c,t):
    return 30*m.exp(-0.5/(t+273))*c -0.5*(t-20)


def euler(c,T,t):
    for i in range(2):
        c_ant=c
        T_ant=T
        c=c_ant+fc(c_ant,T_ant)*t
        T=T_ant+ft(c_ant,T_ant)*t
        print("{} iteração, T: {} C: {}".format(i,T,c))


def rk4(c,T,t):
    for i in range(2):
        c_ant=c
        T_ant=T

        dT1=t*ft(c_ant,T_ant)
        dc1=t*fc(c_ant,T_ant)

        dT2=t*ft(c_ant+dc1/2,T_ant+dT1/2)
        dc2=t*fc(c_ant+dc1/2,T_ant+dT1/2)

        dT3=t*ft(c_ant+dc2/2,T_ant+dT2/2)
        dc3=t*fc(c_ant+dc2/2,T_ant+dT2/2)
        
        dT4=t*ft(c_ant+dc3,T_ant+dT3)
        dc4=t*fc(c_ant+dc3,T_ant+dT3)

        T=T_ant+dT1/6+dT2/3+dT3/3+dT4/6
        c=c_ant+dc1/6+dc2/3+dc3/3+dc4/6
        print("{} iteração, T: {} C: {}".format(i,T,c))

print("euler:")
euler(2.5,25,0.25)
print("rk4:")
rk4(2.5,25,0.25)