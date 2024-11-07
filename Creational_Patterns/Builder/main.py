from concrete_builder import GamingComputerBuilder, OfficeComputerBuilder
from director import ComputerDirector

gaming_builder = GamingComputerBuilder()
director = ComputerDirector(gaming_builder)
gaming_computer = director.construct_computer()
print(gaming_computer)

office_builder = OfficeComputerBuilder()
director = ComputerDirector(office_builder)
office_computer = director.construct_computer()
print(office_computer)
