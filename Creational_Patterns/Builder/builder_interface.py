from abc import ABC, abstractmethod

class ComputerBuilder(ABC):

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_gpu(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass

