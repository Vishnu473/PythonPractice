# 3. Check that a tuple type cannot be changed in python.

tup1 = (34,12,45)

tup1[2] = 30 #Throws Error, as the tuple cannot be modified/changed - as tuple is immutable.

print(tup1)