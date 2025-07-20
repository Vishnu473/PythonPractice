# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.12)
s.add('20') # length of s after these operations?


print(len(s),s)

# Here, the length will be just 2. This is because both the 20 and 20.0 are same in terms of value that is 20. It will be 3 if we have something like 20.12
