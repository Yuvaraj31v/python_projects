from pytreemap import TreeSet
from ordered_set import OrderedSet

# HashSet
#  works as tree set when integers are being stored
sets = set()

sets.add("a")
sets.add("c")  # return type none
sets.add("e")
sets.add("b")

print(sets)

int_set = {2}
int_set.add(1)
int_set.add(5)
int_set.add(2)
int_set.add(4)

print(int_set)

# TreeSet

tree_set = TreeSet()

tree_set.add("a")  # return type boolean
tree_set.add("c")

tree_set.add("d")

print(tree_set)

# Linked_Hash_set

Linked_set = OrderedSet()
Linked_set.add("a")  # return type 1 if true 0 for false
Linked_set.add("a")
Linked_set.add("b")

print(Linked_set)
