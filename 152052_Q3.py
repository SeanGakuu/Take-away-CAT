class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, registration_number, make, model, num_seats):
        super().__init__(registration_number, make, model)
        self.num_seats = num_seats

    def __str__(self):
        return super().__str__() + f", Type: Car, Seats: {self.num_seats}"


class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return super().__str__() + f", Type: Truck, Capacity: {self.cargo_capacity} tons"


class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return super().__str__() + f", Type: Motorcycle, Engine Capacity: {self.engine_capacity} cc"


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle '{vehicle.make} {vehicle.model}' added successfully.\n")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.\n")
        else:
            print("List of Vehicles:")
            for vehicle in self.vehicles:
                print(vehicle)
            print()

    def search_vehicle(self, registration_number):
        found = False
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print("Vehicle found:")
                print(vehicle)
                found = True
                break
        if not found:
            print(f"Vehicle with registration number '{registration_number}' not found.\n")


def main():
    fleet = Fleet()

    # Adding vehicles
    car1 = Car("KDA001A", "Mercedes-AMG", "S63 E-Performance", 4)
    fleet.add_vehicle(car1)

    truck1 = Truck("KDA002A", "Volvo", "FH16", 20)
    fleet.add_vehicle(truck1)

    motorcycle1 = Motorcycle("KMDA0001", "Yamaha", "R1M", 1000)
    fleet.add_vehicle(motorcycle1)

    # Displaying all vehicles
    fleet.display_vehicles()

    # Searching for a vehicle
    fleet.search_vehicle("KDA001A")
    fleet.search_vehicle("KDB420A")

if __name__ == "__main__":
    main()
