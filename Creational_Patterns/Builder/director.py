from builder_interface import ComputerBuilder

class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_cpu()
        self.builder.build_memory()
        self.builder.build_storage()
        self.builder.build_gpu()
        return self.builder.get_computer()
