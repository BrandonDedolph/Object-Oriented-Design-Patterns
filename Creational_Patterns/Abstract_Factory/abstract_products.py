from abc import ABC, abstractmethod

# Abstract product for a button
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Abstract product for a checkbox
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass
