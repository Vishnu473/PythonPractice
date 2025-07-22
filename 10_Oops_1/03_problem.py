# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class Example:

    a = 10

    def findA(cls):
        return cls.a

object = Example()
object.a = 0
print(Example.a)

