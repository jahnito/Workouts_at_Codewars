'''
I don't like writing classes like this:

class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color

Give me the power to create a similar class like this:

Animal = make_class("name", "species", "age", "health", "weight", "color")
'''




def make_class(*args):

    def animal(args):
        class Animal:
            def __init__(self, name, species, age, health, weight, color):
                self.name = name
                self.species = species
                self.age = age
                self.health = health
                self.weight = weight
                self.color = color
        
    return animal


if __name__ == '__main__':
    Animel = make_class("name", "species", "age", "health", "weight", "color")
    print(Animel)
