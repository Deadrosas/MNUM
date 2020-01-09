def f(x,y):
    return pow(y,2)-2*x*y-6*y+2*pow(x,2)+12

def fx(x,y):
    return -2*y+4*x

def fy(x,y):
    return 2*y-2*x-6

def fxx(x,y):
    return 4

def fxy(x,y):
    return -2

def fyx(x,y):
    return -2

def fyy(x,y):
    return 2


def gradient_and_powell(x,y,learning_rate,tol=1e-5):
    """Gradient method
    to find the minimum of a function
    f: a strictly unimodal function on [a,b]

    Example:
    >>> f = pow(y,2)-2*x*y-6*y+2*pow(x,2)+12
    >>> x0 = 1
    >>> y0 = 1
    >>> learning_rate = 0.1
    >>> z = gradient(1, 1, 0.1)
    >>> z = 0.00017

    """
    z0=f(x,y)
    x=x-learning_rate*fx(x,y)
    y=y-learning_rate*fy(x,y)
    z=f(x,y)
    for i in range(20):
        for i in range(20):
            if(z<z0):
                learning_rate=learning_rate*2
                z0=f(x,y)
                x=x-learning_rate*fx(x,y)
                y=y-learning_rate*fy(x,y)
                z=f(x,y)
            else:
                learning_rate=learning_rate/2
            print("x:",x,"y:",y,"z0:",z0,"z",z,"h:",learning_rate)
        x_ant=x
        y_ant=y
        det=fxx(x,y)*fyy(x,y)-fxy(x,y)*fyx(x,y)
        x=x_ant-(fyy(x_ant,y_ant)*fx(x_ant,y_ant)-fxy(x_ant,y_ant)*fy(x_ant,y_ant))/det
        y=y_ant-(-fxy(x_ant,y_ant)*fx(x_ant,y_ant)+fxx(x_ant,y_ant)*fy(x_ant,y_ant))/det
        print(x,y)
    return z

print(gradient_and_powell(7,5,0.005))