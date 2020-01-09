import math
def f(x,y):
    return math.sin(y)+y*y/4+math.cos(x)+x*x/4-1

def fx(x,y):
    return x/2-math.sin(x)

def fy(x,y):
    return math.cos(y)+y/2


def fxx(x,y):
    return 1/2-math.cos(x)

def fxy(x,y):
    return 0

def fyx(x,y):
    return 0

def fyy(x,y):
    return 1/2-math.sin(y)


def Hess(x,y):
    for i in range(20):
        x_ant=x
        y_ant=y
        det=fxx(x,y)*fyy(x,y)-fxy(x,y)*fyx(x,y)
        x=x_ant-(fyy(x_ant,y_ant)*fx(x_ant,y_ant)-fxy(x_ant,y_ant)*fy(x_ant,y_ant))/det
        y=y_ant-(-fxy(x_ant,y_ant)*fx(x_ant,y_ant)+fxx(x_ant,y_ant)*fy(x_ant,y_ant))/det
        print(x,y)
    return [x,y]

print(Hess(0,0))