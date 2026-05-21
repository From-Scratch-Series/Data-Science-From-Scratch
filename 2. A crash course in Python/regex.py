import re

re_examples = [
    not re.match('a','cat'), # cat doesn't start with a
    re.search('a','dad'),    # dad has d in it
    4 == len(re.split('[ab]','madebad')),
    'A-B-' == re.sub('[0-9]','-','A2B4')
]
assert all(re_examples) #all regex eg should be True

print(re.split('[ab]','madebad'))