# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __len__(self):
        return 3
    
vector1 = Vector(2,3,4)
vector2 = Vector(5,1,-2)

print(f"The sum of two Vectors {vector1} and {vector2} is {vector1 + vector2}")
print(f"The dot product of two Vectors {vector1} and {vector2} is {vector1 * vector2}")
print(f"The length of the vector {vector1} is {len(vector1)} and vector {vector2} is {len(vector2)}")