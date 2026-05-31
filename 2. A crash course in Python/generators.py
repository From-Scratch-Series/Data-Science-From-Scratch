def square_num(nums):
    new = []
    for i in nums:
        new.append(i*i)
    return new

nums = [1,2,3,4,5]
print(square_num(nums))

#using generator function
def square_num_gen(nums):
    for i in nums:
        yield i*i

print(square_num_gen(nums)) #<generator object square_num_gen at 0x...>
print(next(square_num_gen(nums))) #creates generator_B, execution: y=1; yield=1, generator_B is then discarded
print(next(square_num_gen(nums))) #(NO CHANGE) creates generator_C (a new generator), again starts from beginning, so same execution: y=1; yield=1, generator_C is also discarded

print('-'*10)
#now next() works, since next() is called on same generator my_nums 
my_nums = square_num_gen(nums)
print(next(my_nums)) 
print(next(my_nums))
print(next(my_nums))
for num in my_nums:
    print(num, end=' ')
print()
print('-'*10)

my_nums = square_num_gen(nums)
print(my_nums.__next__())
print(my_nums.__next__())
print(my_nums.__next__())
for num in my_nums:
    print(num, end= ' ')
print()

print('-'*20)

#using generator expression
my_nums = (x*x for x in nums) #returns a generator as we have () instead of []
print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(my_nums.__next__())

print('-'*20)
print(next((x*x for x in nums)))
print(next((x*x for x in nums)))#no change, since, a completely new generator is created




