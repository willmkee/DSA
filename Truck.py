class Truck:
    # Truck constructor
    def __init__(self, capacity, speed, packages, mileage, current_location, depart_time, current_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.current_location = current_location
        self.depart_time = depart_time
        self.current_time = current_time

    # Add package to truck
    def add_package(self, package):
        if len(self.packages) < self.capacity:  # Make sure there is room for the package
            self.packages.append(package)  # Append the package to the package list
            return True
        else:
            return False

    # Remove package from truck
    def remove_package(self, package):
        self.packages.remove(package)

    # Truck string constructor
    def __str__(self):
        return f"Capacity: {self.capacity} \nMileage: {self.mileage:.2f} miles\n" \
               f"Current Location: {self.current_location}\nDeparture Time: {self.depart_time}\n" \
               f"Packages: {[package.package_id for package in self.packages]}"
