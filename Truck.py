


class Truck:
    def __init__(self, capacity, packages, mileage, current_location, depart_time, current_time):
        self.capacity = capacity
        self.packages = packages
        self.mileage = mileage
        self.current_location = current_location
        self.depart_time = depart_time
        self.current_time = current_time

    def __str__(self):
        return f"Capacity: {self.capacity} \nMileage: {self.mileage:.2f} miles\n" \
               f"Current Location: {self.current_location}\nDeparture Time: {self.depart_time}\n" \
               f"Packages: {[package.package_id for package in self.packages]}"


