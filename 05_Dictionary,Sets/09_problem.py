# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

print(s)

# First, the set is not a valid one.
# As list cannot be inside a set as a value. So, It gives Type Error - "UnHashable List" This is because, the lists are mutable and not hashable.
# No, We cannot access the set's values. So We cannot change the values inside a list(as list is inside the set as a value).

# Even if you have tuple inplace of list to make the set valid, as the tuples are immutable, You cannot change the values inside the tuple. as the tuples are immutable and hashable.