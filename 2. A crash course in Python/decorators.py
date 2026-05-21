#reference 'visually explained' yt channel

import time

#decrator is a function which takes in a func, modifies the base func and return a enhanced/modified func
#decorator function
def time_taken(base_fn):
    def enhanced_fn(*args, **kwargs): #*args and **kwargs so that base fn definition can be flexible, with any no. of args and keyword args
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Task time:{end_time - start_time} seconds")
    return enhanced_fn

def brew_tea():
    print('Brewing tea...')
    time.sleep(1)
    print('tea is ready')

brew_tea = time_taken(brew_tea) #manual way to enhance the func
brew_tea() 

@time_taken #via @ notation to enchance the fn
def make_tea(tea_type, sec):
    print(f'making {tea_type} tea')
    time.sleep(sec)
    print('tea is ready')

make_tea('green', 1)
make_tea(tea_type='mocha',sec=2) 
make_tea('kahwa', sec=3) #positional and keyword args together
