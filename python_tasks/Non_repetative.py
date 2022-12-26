from pytreemap import TreeSet

tree_set = TreeSet()
string = input()
output = []
for i in string:

    if tree_set.add(i) == True:
        output.append(i)
    else:
       output.remove(i)
print(output)
