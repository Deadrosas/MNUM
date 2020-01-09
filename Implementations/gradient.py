def f(x,y):
    return pow(y,2)-2*x*y-6*y+2*pow(x,2)+12

def fx(x,y):
    return -2*y+4*x

def fy(x,y):
    return 2*y-2*x-6

def gradient(x,y,learning_rate,tol=1e-5):
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
    for i in range(0,50):
        if(z<z0):
            learning_rate=learning_rate*2
            z0=f(x,y)
            x=x-learning_rate*fx(x,y)
            y=y-learning_rate*fy(x,y)
            z=f(x,y)
        else:
            learning_rate=learning_rate/2
        print("x:",x,"y:",y,"z0:",z0,"z",z,"h:",learning_rate)
    return z

print(gradient(7,5,0.005))


