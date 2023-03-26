from Package import Package
from Truck import Truck
import csv
from HashTable import ChainingHashTable


def distanceBetween(streetAddress1, streetAddress2):
    index1 = None
    index2 = None
    for address in address_data:
        if streetAddress1 == address[2]:
            index1 = address_data.index(address)
        if streetAddress2 == address[2]:
            index2 = address_data.index(address)
    if index1 is None or index2 is None:
        print("One or both of the addresses not found in addressData.")
    if index1 > index2:
        distance = distance_data[index1][index2]
    else:
        distance = distance_data[index2][index1]
    return float(distance)


def load_packages(fileName):  # Method to load packages into Hash Table
    # Opens csv file
    with open(fileName) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)
        # Iterates through each row in csv file and assigns package variables
        for row in package_data:
            package_id = int(row[0])
            package_address = row[1]
            package_city = row[2]
            package_state = row[3]
            package_zip = row[4]
            package_deadline = row[5]
            package_weight = row[6]
            delivery_time = None
            package_status = "At Hub"

            # Creates new package object
            p = Package(package_id, package_address, package_city, package_state,
                        package_zip, package_deadline, delivery_time, package_weight, package_status)

            # Inserts package into hash table
            myHash.insert(package_id, p)


def loadDistanceData(distanceData):
    with open('distanceCSV.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            distanceData.append(row)


def loadAddressData(addressData):
    with open('addressCSV.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            addressData.append(row)


def minDistanceFrom(truck):
    current_address = truck.current_location
    min_distance = float('inf')
    next_location = None
    for package in truck.packages:
        if distanceBetween(current_address, package.delivery_address) < min_distance:
            min_distance = distanceBetween(current_address, package.delivery_address)
            next_location = package.delivery_address
    return next_location


def truckDeliverPackages(truck):
    while len(truck.packages) > 0:
        truck.mileage += distanceBetween(truck.current_location, minDistanceFrom(truck))
        truck.current_location = minDistanceFrom(truck)
        for package in truck.packages:
            if package.delivery_address == truck.current_location:
                package.delivery_status = "Delivered"
                package.delivery_time = "Current Time"  # FIX ME
                print(package)
                truck.remove_package(package)

    truck.mileage += distanceBetween(truck.current_location, "4001 South 700 East")
    truck.current_location = "4001 South 700 East"
    print(truck)


# Creates Hash Table
myHash = ChainingHashTable()

# Loads packages into hash table from packageCSV.csv
load_packages('packageCSV.csv')

# Create distance_data list to hold distances
distance_data = []
# Load distances into distance_data array
loadDistanceData(distance_data)

address_data = []
loadAddressData(address_data)

truck1 = Truck(16, 18, [], 0, "4001 South 700 East", "8:00 AM", "8:00")
truck2 = Truck(16, 18, [], 0, "4001 South 700 East", "8:00 AM", "8:00")

for i in range(1, 17):
    truck1.add_package(myHash.search(i))

truckDeliverPackages(truck1)