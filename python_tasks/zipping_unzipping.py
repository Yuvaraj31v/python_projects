from itertools import zip_longest

listA = [1, 2, 3, 4]
listB = ['a', 'b', 'c', 'd']

zl = zip(listA, listB)

zl = list(zl)

print(zl)

listC, listD = zip(*zl)

print(listC)

print(listD)

print(listA)

print(listB)

# with different length size of the list
numbers = [1, 2, 3]
letters = ['a', 'b', 'c', 'd']
longest = range(5)
zipped = zip_longest(numbers, letters, fillvalue='?')

# iterate a zipped file
for i, j in zipped:
    print(i, j)
print(list(zipped))
