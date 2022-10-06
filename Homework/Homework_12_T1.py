def Animal_Communication(animal):
    print(animal.animal_say_hello())

class Animal:
    def animal_say_hello():
        pass

class Dog(Animal):
    def animal_say_hello(self):
        print("Mellow")

class Cat(Animal):
    def animal_say_hello(self):
        print("Hellow")

c = Cat()
d = Dog()


Animal_Communication(c)
Animal_Communication(d)