# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:

    def __init__(self, name, exp, company):
        self.name = name
        self.exp = exp
        self.company = company
    
    def print(self):
        return f"{self.name} working at {self.company} and has experience of {self.exp}(years)"
    

Prg1 = Programmer('Rajesh',2,'Microsoft')
print(Prg1.print())