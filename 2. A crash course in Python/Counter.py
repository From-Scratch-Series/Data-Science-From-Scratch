from collections import Counter

digit_counts = Counter([1,2,1,0,3,3,3,4])
print(digit_counts)

#3 most common words
print(digit_counts.most_common(3))

for k,v in digit_counts.most_common(3):
    print(f"{k} is duplicated {v} times")
