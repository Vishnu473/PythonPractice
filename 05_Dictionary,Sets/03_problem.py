# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

# Yes, we can have the same value as both integer and string as the value treated are integer and strings.

s= set()

s.add(18)
s.add('18')

print(s)