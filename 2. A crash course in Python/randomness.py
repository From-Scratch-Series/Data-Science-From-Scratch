import random

# random.seed(42)
x = [random.random() for _ in range(4)]

# random.seed(42)
print(random.random())
# random.seed(42)
print(random.random()) #same is seed was same

print(random.randrange(10))
print(random.randrange(3,6))

nums = [1,2,3,4,5,6,7]
random.shuffle(nums)
print(nums)


x = random.choice(['Alice', 'Bob', 'Charlie']) 
print(x)

x = range(50)
y = random.sample(x,6) #wihout replacement i.e no duplicates
print(y)

y = [random.choice(range(15)) for _ in range(10)] #random.choice() is 'with replacement' i.e duplicates can occur
print(y)