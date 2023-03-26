from utils import distanceBetween


class Truck:
    def __init__(self, capacity, speed, packages, mileage, current_location, depart_time, current_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.current_location = current_location
        self.depart_time = depart_time
        self.current_time = current_time

    def add_package(self, package):
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        else:
            return False

    def minDistanceFrom(self):
        current_address = self.current_location
        min_distance = float('inf')
        next_location = None
        for Package in self.packages:
            if distanceBetween(current_address, Package.delivery_address()) < min_distance:
                min_distance = distanceBetween(current_address, Package.delivery_address())
                next_location = Package.delivery_address()
        return next_location



    def __str__(self):
        return f"Capacity: {self.capacity} \nMileage: {self.mileage:.2f} miles\n" \
               f"Current Location: {self.current_location}\nDeparture Time: {self.depart_time}\n" \
               f"Packages: {[package.package_id for package in self.packages]}"


