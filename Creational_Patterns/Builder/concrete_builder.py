from builder_interface import ComputerBuilder
from product import Computer

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "Intel i9"

    def build_memory(self):
        self.computer.memory = "32GB DDR4"

    def build_storage(self):
        self.computer.storage = "1 TB SSD"

    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 3080"

    def get_computer(self):
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "Intel i5"
        
    def build_memory(self):
        self.computer.memory = "16GB DDR4"
        
    def build_storage(self):
        self.computer.storage = "500GB SSD"
        
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"
        
    def get_computer(self):
        return self.computer

