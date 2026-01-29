class Dog:
    def __init__(self, name, raca):
        self.name = name
        self.raça = raca

    def bark(self):
        print(f"Woof! {self.name} e eu sou da raça {self.raça}.")


my_dog = Dog("Osvaldo", "Labrador")

my_dog.bark()