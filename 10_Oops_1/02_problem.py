# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:

    def __init__(self,number):
        self.number = number
    
    def square_num(self):
        return f"The sqaure of {self.number} is {self.number*self.number}"
    
    def cube_num(self):
        return f"The cube of {self.number} is {self.number*self.number*self.number}"
    
    def square_root_num(self):
        return f"The sqaure root of {self.number} is {self.number**(0.5)}"
    

calc = Calculator(3)
print(calc.square_num())
print(calc.cube_num())
print(calc.square_root_num())