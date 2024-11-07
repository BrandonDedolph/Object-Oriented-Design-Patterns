from creator_abstract_class import AnimalFactory
from concrete_creators import DogFactory, CatFactory

def get_animal_speak(factory: AnimalFactory):
    animal = factory.create_animal()
    return animal.speak()


dog_factory = DogFactory()
print(get_animal_speak(dog_factory))

cat_factory = CatFactory()
print(get_animal_speak(cat_factory))
