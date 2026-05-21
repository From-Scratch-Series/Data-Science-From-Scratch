from Counter import digit_counts

x = [3,5,4,1]
y = sorted(x) #doesn't change the original
print(x,y)

x.sort() #changes the original
print(x)

x = sorted([-4,2,-1,3,-2], key=abs, reverse=True)
print("sort by absolute value in descending order", x)

y = sorted(digit_counts.items(), key = lambda x: x[1], reverse=True)
print(y)