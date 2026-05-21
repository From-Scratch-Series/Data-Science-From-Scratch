#all- outputs True is all elements are Truthy
#any- outputs True is any elements is  Truthy 

a = any([False, {}, (0),[],'',set(),0.0,None]) #(0) is not a tuple, (0,) is a tuple
b = all([True, 1,{3},(0,), [0], -1, 3.3])
c = all([]) #no falsy values in the list hence, True
print(a,b,c)

X = None
assert X== None
assert X is None