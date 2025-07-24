# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self, species):
        self.name = species

class Pets(Animals):
    def __init__(self,species,isPet):
        super().__init__(species)
        self.isPet = isPet

    def __str__(self):
        return f"{self.name} is a {self.isPet} animal."


class Dog(Pets):
    def __init__(self, species, isPet, name):
        super().__init__(species, isPet)
        self.name = name

    def bark(self):
        return f"{self.name} says Bow Bow!"
    
class Lion(Pets):
    def __init__(self, species, isPet, name):
        super().__init__(species, isPet)
        self.name = name

    def roar(self):
        return f"{self.name} and it says Roar!"
    
dog = Dog("Dog", "Pet","Harry")
print(dog)
print(dog.bark())

lion = Lion("Lion", "Wild", "Simba")
print(lion)
print(lion.roar())