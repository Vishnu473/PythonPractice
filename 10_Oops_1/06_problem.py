# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

# Yes, we can change the parameter name from 'self' to 'harry' or to anyother name.

class Person1:

    def __init__(self,name):
        self.name = name

    def show_name(self):
        print(f'The name of the person is {self.name}')

person1 = Person1('Vishnu')
person1.show_name()


class Person2:

    def __init__(harry,name):
        harry.name = name

    def show_name(harry):
        print(f'The name of the person is {harry.name}')

person2 = Person2('Kishore')
person2.show_name()