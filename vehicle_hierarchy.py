# Base class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def description(self):
        return f"{self.brand} vehicle with {self.wheels} wheels"


# Child class: Car
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 4)

    def description(self):
        return f"Car: {self.brand}, 4 wheels"


# Child class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)

    def description(self):
        return f"Motorcycle: {self.brand}, 2 wheels"


# Child class: Truck
class Truck(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 6)

    def description(self):
        return f"Truck: {self.brand}, 6 wheels"


def main():
    car = Car("Toyota")
    bike = Motorcycle("Yamaha")
    truck = Truck("Tata")

    vehicles = [car, bike, truck]

    for v in vehicles:
        print(v.description())

    print("\nNote: super() was used to reuse Vehicle.__init__ in child classes.")


if __name__ == "__main__":
    main()