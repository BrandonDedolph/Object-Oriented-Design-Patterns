from concrete_products import Dog, Cat
from creator_abstract_class import AnimalFactory
from product_interface import Animal

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()
