even_num = [x for x in range(5) if x%2==0]
squares = [x*x for x in range(5)]
even_squares = [x*x for x in even_num]
pairs = [(x,y) for x in range(5) for y in range(5)]
increasing_pairs = [(x,y) for x in range(5) for y in range(x+1,5)]

print(even_num)
print(squares)
print(even_squares)
print(pairs,'\n')
print(increasing_pairs)

square_dict = {x:x*x for x in range(5)}
square_set  = {x*x for x in [1,-1]}

print(square_dict)
print(square_set)

zeros = [0 for _ in range(5)]
print(zeros)