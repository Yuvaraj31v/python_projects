from pytreemap import TreeSet

tree_set = TreeSet()
string = input()
output = {}
for i in string:
    if tree_set.add(i):
        output[i] = 1
    else:
        output[i] = output[i] + 1
print(output)
