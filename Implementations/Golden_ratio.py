def f(x):
    return pow(x-4,2)+pow(x,4)

#---------------------------------------------Iterative Algorithms------------------------------------------------#
"""Python program for golden section search.  This implementation
   does not reuse function evaluations and assumes the minimum is c
   or d (not on the edges at a or b)"""
import math
gn = (math.sqrt(5) + 1) / 2 #Golden Number

def gss(f, a, b, tol=1e-5):
    """Golden section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    Example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1, 5)
    >>> x
    2.000009644875678

    """
    #We calculate C we the Golden Number but we can alo calculate with the golden ratio like this 
    c = b - (b - a) /gn
    d = a + (b - a) / gn
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # We recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        c = b - (b - a) / gn
        d = a + (b - a) / gn

    return (b + a) / 2

"""Python program for golden section search.  This implementation
   reuses function evaluations, saving 1/2 of the evaluations per
   iteration, and returns a bounding interval."""

invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2

def gss2(f, a, b, tol=1e-5):
    """Golden section search.

    Given a function f with a single local minimum in
    the interval [a,b], gss returns a subset interval
    [c,d] that contains the minimum with d-c <= tol.

    Example:
    >>> f = lambda x: (x-2)**2
    >>> a = 1
    >>> b = 5
    >>> tol = 1e-5
    >>> (c,d) = gss2(f, a, b, tol)
    >>> print(c, d)
    (1.9999959837979107, 2.0000050911830893)
    """

    (a, b) = (min(a, b), max(a, b))
    h = b - a
    if h <= tol:
        return (a, b)

    # Required steps to achieve tolerance
    n = int(math.ceil(math.log(tol / h) / math.log(invphi)))

    c = a + invphi2 * h
    d = a + invphi * h
    yc = f(c)
    yd = f(d)

    for k in range(n-1):
        if yc < yd:
            b = d
            d = c
            yd = yc
            h = invphi * h
            c = a + invphi2 * h
            yc = f(c)
        else:
            a = c
            c = d
            yc = yd
            h = invphi * h
            d = a + invphi * h
            yd = f(d)

    if yc < yd:
        return (a, d)
    else:
        return (c, b)

#-----------------------------------------Recursive Algorithm-----------------------------------------------------#
invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2

def gssrec(f, a, b, tol=1e-5, h=None, c=None, d=None, fc=None, fd=None):
    """ Golden section search, recursive.

    Given a function f with a single local minimum in
    the interval [a,b], gss returns a subset interval
    [c,d] that contains the minimum with d-c <= tol.

    Example:
    >>> f = lambda x: (x-2)**2
    >>> a = 1
    >>> b = 5
    >>> tol = 1e-5
    >>> (c,d) = gssrec(f, a, b, tol)
    >>> print (c, d)
    (1.9999959837979107, 2.0000050911830893)
    """

    (a, b) = (min(a, b), max(a, b))
    if h is None: h = b - a
    if h <= tol: return (a, b)
    if c is None: c = a + invphi2 * h
    if d is None: d = a + invphi * h
    if fc is None: fc = f(c)
    if fd is None: fd = f(d)
    if fc < fd:
        return gssrec(f, a, d, tol, h * invphi, c=None, fc=None, d=c, fd=fc)
    else:
        return gssrec(f, c, b, tol, h * invphi, c=d, fc=fd, d=None, fd=None)

print(gss(lambda x:math.sin(x**2),0.006904,0.013584,1e-7))