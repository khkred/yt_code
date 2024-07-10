my_set = set([1, 2, 2, 3, 4, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)

print(my_set)

my_set.remove(2)

print(my_set)

# We can also use discard method to remove an element in set
my_set.discard(4)
print(my_set)

my_set2 = {9,8,7}

print(type(my_set2))