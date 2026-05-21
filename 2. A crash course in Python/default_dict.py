from collections import defaultdict

chars = ['a','b','c','a','c','a','c','d']

counts = defaultdict(int)
for c in chars:
    counts[c] += 1
print(counts)

dd_list = defaultdict(list)
dd_list[2] = [1]
dd_list[2] = [2]
dd_list[2].append(1)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict['city']['siliguri'] = {'village': 'bagdogra'}
print(dd_dict)

dd_pair = defaultdict(lambda:[0,0])
dd_pair[2][0] = 3
dd_pair[2][1] = 2
print(dd_pair)
