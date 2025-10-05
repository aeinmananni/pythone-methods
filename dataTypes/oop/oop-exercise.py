class Animal:
    zoo_name: str = "Zoo"

    def __init__(self, name: str, species: str, age: int, sound: str):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says: {self.sound}"
    
    def info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Zoo: {Animal.zoo_name}"
    
    def __str__(self):
        return self.info()


class Bird(Animal):
    def __init__(self, wing_span: str, name: str, species: str, age: int, sound: str):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} (a bird) chirps: {self.sound}"



shir = Animal(name="Shir", species="Vahshi", age=4, sound="Roar")
print(shir)
print(shir.make_sound())

bird1 = Bird(name="Parandeh", species="Parandegan", age=1, sound="Tweet", wing_span="123 cm")
print(bird1)
print(bird1.make_sound())
