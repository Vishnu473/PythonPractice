# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vector((self.x + other.x),(self.y + other.y), (self.z + other.z))

    def __mul__(self,other):
        return (self.x * other.x)+(self.y * other.y)+(self.z * other.z)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
vector1 = Vector(2,3,4)
vector2 = Vector(5,1,-2)

print(f"The sum of two Vectors {vector1} and {vector2} is {vector1 + vector2}")
print(f"The dot product of two Vectors {vector1} and {vector2} is {vector1 * vector2}")