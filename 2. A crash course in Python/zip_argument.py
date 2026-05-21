list1 = ['a','b','c']
list2 = [1,2,3]

x = list(zip(list1,list2))
print(*x)
print(x)
list1, list2 = zip(*x) #unzip
list1, list2 = zip(('a', 1), ('b', 2), ('c', 3)) #same thing as *x
print(list1, list2)
print(type(list1), type(list2))#tuple now

def add(a,b): return a+b
print(add(*[1,2])) #argument unpacking
