class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound made by the animal")

class Mammal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Dog(Animal,Mammal):
    def __init__(self,name,breed,color):
        Animal.__init__(self,name,species="Dog")
        Mammal.__init__(self,name,color)  
        self.breed = breed

    def make_sound(self):
        print("Bark!!!!")      

obj = Dog("Uday","Husky","White")
print(obj.species)