#reference- 'corey schafer' yt channel

#iterables: something we can iterate on, has __iter__() as its method
#iterator:  an object inside an iterable, it stores its state to know where it is in the iteration process, it also has __next__() method to check the next item in the iterable

nums = [1,2,3]

print(dir(nums)) #has a __iter__ hence it is an iterable
# print(next(nums)) #error, becuase list is not an iterator

i_nums = nums.__iter__() #returns as iterator
i_nums = iter(nums) #same as nums.__iter__()
print(dir(i_nums)) #since its an iterator, it has __next__() method, it has __iter__() method as well, strange?, an iterator is also an iteratable, here it will output itself

while True:
    try:
        print(next(i_nums))
    except StopIteration:
        break


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)
# for num in nums:
#      print(num, end=' ')
while True:
    try:
        print(next(nums), end=' ')
    except StopIteration:
        break
print('\n')

#Generators are a type of iterables only
#Generator helps with automatic creation of __iter__ and __next__
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
    
nums = my_range(1, 10)
while True:
    try:
        print(next(nums), end=' ')
    except StopIteration:
        break
print('\n')
for num in nums:
    print(num, end=' ')
