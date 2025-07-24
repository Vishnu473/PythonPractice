# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class  Vector2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
object_3d = Vector3D(1, 2, 3)
print(object_3d)  # Output: 1i + 2j + 3