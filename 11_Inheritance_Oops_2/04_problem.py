# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real,imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}j"
    
    def __add__(self,other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self,other):
        real_part = (self.real*other.real) - (other.imag*self.imag)
        imag_part = (self.real*other.imag) + (self.imag*other.real)
        return Complex(real_part,imag_part)
    
comp_num1 = Complex(-2,3)
comp_num2 = Complex(1,-1)

print(f"The addition of {comp_num1} and {comp_num2} is {comp_num1+comp_num2}")
print(f"The multiplication of {comp_num1} and {comp_num2} is {comp_num1*comp_num2}")