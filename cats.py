class Cat:
# CLASS ATTRIBUTE - applies to all cats!
    species = "Mammal"

# INSTANCES ATTRIBUTES - different for each instance of cat
# self means it is pointing back to itself (the class of cat)
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
    
# INSTANCE METHOD - different for each instance of cat    
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

gus = Cat("Gus", 10)
beans = Cat("Beans", 11)
print(gus.name)
print(gus.age)
print(gus.species)

print(gus.description())
print(beans.description())