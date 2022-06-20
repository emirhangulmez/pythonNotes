# Python Refreshing
# Author: Emirhan Gulmez

class Musician:

    job = "Musician"

    def __init__(self, name, age, instrument):
        self.name = name
        self.age = age
        self.instrument = instrument

    def sing(self):
        print("sing sang song", self.instrument)
        return f"sing sang song {self.instrument}"

    def __len__(self):
        return self.age

    def __str__(self):
        return self.name


james = Musician("James", 30, "Guitar")  # Instance
james.sing()


# Inheritance
class OtherMusician(Musician):

    def __int__(self):
        Musician.__init__(self, self.name, self.age, self.instrument)


attempt = OtherMusician("attempt", 50, "Flute")
attempt.sing()


# Polymorphism

class Dog:
    def __init__(self, name):
        self.name = name

    def information(self):
        return f"I am dog and my name is {self.name}"


class Cat:
    def __init__(self, name):
        self.name = name

    def information(self):
        return f"I am cat and my name is {self.name}"


classList = [Dog("Bars"), Cat("Tom")]
for pets in classList:
    print(pets.information())
