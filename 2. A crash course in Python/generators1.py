from math import sqrt

def gen_values():
    # yield 1
    # yield 2
    # yield 3
    for i in [1,2,3]:
        yield i

#for loop, automatically calls next(), and exits loop automatically without StopIterationError
for i in gen_values():
    print(i, end=' ') 
print()

#usual function
#eager evaluation
def get_primes_list(start,end):
    primes = []
    for num in range(start,end+1):
        if num < 2:
            continue
        for i in range(2,int(sqrt(num))):
            if num % i == 0:
                break
        else:#else of for loop
            primes.append(num)
    return primes

# primes = get_primes_list(10, 1000000) #computationally time taking and can block the thread
# print(primes)

#using generators to extract the value one at a time only when needed
#lazy evaluation
def generate_primes(start, end):
    for num in range(start, end+1):
        if num < 2:
            continue
        for i in range(2,int(sqrt(num))):
            if num % i == 0:
                break
        else:
            yield num 

primes = generate_primes(80, 1000000000)
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
#we can use for loop to generate all values from the generator
