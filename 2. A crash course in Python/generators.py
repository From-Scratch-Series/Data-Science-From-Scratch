def square_num(nums):
    new = []
    for i in nums:
        new.append(i*i)
    return new

nums = [1,2,3,4,5]
print(square_num(nums))

#using generator
def square_num_gen(nums):
    for i in nums:
        yield i*i
print(square_num_gen(nums))
print(next(square_num_gen(nums)))
print(next(square_num_gen(nums))) #no change

my_nums = square_num_gen(nums)
print(my_nums.__next__())
print(my_nums.__next__())
print(my_nums.__next__())
for num in my_nums:
    print(num, end= ' ')
print('')

my_nums = (x*x for x in nums) #returns a generator as we have () instead of []
print(my_nums)




