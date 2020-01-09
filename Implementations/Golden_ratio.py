def f(x):
    return pow(x-4,2)+pow(x,4)

import math
#Golden Number
gn = (math.sqrt(5) + 1) / 2 

def golden_method(a,b,tolerance=1e-4):
    while(abs(a-b)>tolerance):
        #We calculate C we the Golden Number but we can alo calculate with the golden ratio like this:
        c = b - (b - a) /gn
        d = a + (b - a) / gn
        if(f(c)>f(d)):
            a=c
        else:
            b=d
    return [a,b]

print(golden_method(0,4))