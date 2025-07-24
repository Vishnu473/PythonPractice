# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:

    def __init__(self,name,salary,increment):
        self.name = name
        self.salary = salary
        self.__increment = increment

    def __str__(self):
        return f"{self.name}'s current salary is {self.salary}"

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment/100))
    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        # new slary = old_salary*(1 + (increment/100))
        # increment = ((new_salary/old_salary) -1 )*100
        self.increment = ((salary/self.salary) - 1)*100

# When Employee Joins:
emp1 = Employee("Rajesh",525000,0)
# print(emp1)
print(f"Current Salary is: {emp1.salaryAfterIncrement}") #When Employee sees his salary before Appraisal

# If employee knows the increment and wanna know salary, then:
# emp1.increment = 10
# print(f"Employee's Salary after increment of {emp1.increment} is {emp1.salaryAfterIncrement}")

# To see Increment% after appraisal is based on salary:
emp1.salaryAfterIncrement = 600000
print(f"The % of increment for his new salary of {emp1.salaryAfterIncrement} is {emp1.increment}") #Shows the %increment 