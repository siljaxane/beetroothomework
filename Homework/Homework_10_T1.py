class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

person1 = Person('Maria', 'Musk', 66)

def talk():
    messagae = ('Hello, my name is ', person1.firstname, ' ', person1.lastname, ' and I am', person1.age, 'years old.')




    