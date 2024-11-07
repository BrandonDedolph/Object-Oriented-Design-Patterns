from abc import ABC, abstractmethod
from product_interface import Animal

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
