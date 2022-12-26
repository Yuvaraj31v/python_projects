from collections import OrderedDict
from sortedcontainers import SortedDict
from pytreemap import TreeMap

# HASHMAP
hash_map = {}

hash_map["ajees"] = "3"
hash_map["berlin"] = "1"
hash_map["zaheer"] = "2"

print("hash_map", hash_map)

# LinkedHASHMAP
linked_hash_map = OrderedDict()

linked_hash_map[1] = "1"
linked_hash_map[3] = "1"
linked_hash_map[2] = "1"
print(linked_hash_map)

# TREEMAP
#1.First Method
tree_map = SortedDict()

tree_map[1] = "1"
tree_map[3] = "1"
tree_map[2] = "1"

print(tree_map)

#2.Second Method



#TreeMap
tree_map = TreeMap()

tree_map[1] = "1"
tree_map[3] = "1"
tree_map[2] = "1"

print(tree_map)
