import numpy as np

#higher order func
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x+1

a = doubler(f1)
assert a(2), '2 * (2+1) should equals 6'

def doubler_correct(f):
    def g(*args, **kwargs):
        print(args,kwargs)
        return 2 * f(*args,**kwargs)
    return g

def f2(x,y):
    return x+y

b = doubler_correct(f2)
assert b(1,np.array([2,3])) == [6,8], '2*(1+np.array[2,3]) = 2*np.array[3,4] = [6,8]'

