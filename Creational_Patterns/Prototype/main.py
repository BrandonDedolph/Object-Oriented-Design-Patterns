from prototype import Prototype
from car import Car


def clone():
    # Create protoype manager
    prototype = Prototype()

    # Register a car object
    car = Car("Tesla", "Model S", "Red")
    prototype.register("electric_car", car)

    # Clone the car and customize
    cloned_car = prototype.clone("electric_car", color="Blue", model="Model 3")
    print(cloned_car)


if __name__ == "__main__":
    clone()
