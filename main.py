from Package import Package
from Truck import Truck
import csv
from HashTable import ChainingHashTable
from datetime import timedelta


def distanceBetween(streetAddress1, streetAddress2):  # Method to measure distance between two addresses
    # Initialize indexes for iterating through distance table
    index1 = None
    index2 = None
    # Iterate through addresses to find the indexes of address 1 and 2
    for address in address_data:
        if streetAddress1 == address[2]:
            index1 = address_data.index(address)
        if streetAddress2 == address[2]:
            index2 = address_data.index(address)
    # If either of the addresses are not in the address file, return error message
    if index1 is None or index2 is None:
        print("One or both of the addresses not found in addressData.")
    # Use address indexes to search the distance array
    if index1 > index2:
        distance = distance_data[index1][index2]
    else:
        distance = distance_data[index2][index1]
    # Return the distance as a float
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
            departure_time = None
            special_notes = row[7]

            # Creates new package object
            p = Package(package_id, package_address, package_city, package_state,
                        package_zip, package_deadline, delivery_time, package_weight, package_status, departure_time)

            # Inserts package into hash table
            myHash.insert(package_id, p)

            if package_id in [13, 14, 15, 16, 19, 20]:
                truck1.add_package(p)
                continue
            if "truck 2" in special_notes:
                truck2.add_package(p)
                continue
            if "9:05" in special_notes:
                truck2.add_package(p)
                continue
            if package_id == 9:
                truck3.add_package(p)
                continue
            if package_id in [1, 29, 30, 31, 34, 37, 40]:
                truck1.add_package(p)
                continue
            if "EOD" in package_deadline and len(truck3.packages) < 16:
                truck3.add_package(p)
                continue
            if "EOD" in package_deadline and len(truck2.packages) < 16:
                truck2.add_package(p)
                continue
            raise Exception("Package not loaded: % s" % p.package_id)





def loadDistanceData(distanceData):  # Reads distance data from CSV
    with open('distanceCSV.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            distanceData.append(row)


def loadAddressData(addressData):  # Reads address data from CSV
    with open('addressCSV.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            addressData.append(row)


# Determines which package a truck is carrying needs to be delivered to the nearest location
def minDistanceFrom(truck):
    current_address = truck.current_location
    min_distance = float('inf')
    next_location = None
    # Iterate through packages to determine which package is being delivered to the nearest address
    for package in truck.packages:
        if distanceBetween(current_address, package.delivery_address) < min_distance:
            min_distance = distanceBetween(current_address, package.delivery_address)
            next_location = package.delivery_address
    # Returns string of next address location
    return next_location


def truckDeliverPackages(truck):  # Method to deliver packages and measure truck mileage
    while len(truck.packages) > 0:
        # Update truck mileage based on current location and next location
        distance = distanceBetween(truck.current_location, minDistanceFrom(truck))
        truck.mileage += distance
        # Update current location to the nearest address where a package is to be delivered
        truck.current_location = minDistanceFrom(truck)
        truck.current_time += timedelta(hours=distance / 18)
        # Iterate through packages and if the package is being delivered at current
        # location, remove it from the truck and update delivery time and status
        for package in truck.packages:
            if package.delivery_address == truck.current_location:
                package.delivery_status = "Delivered"
                package.delivery_time = truck.current_time
                package.departure_time = truck.depart_time
                print(package)
                truck.remove_package(package)
    # If truck is empty it returns to the hub
    truck.mileage += distanceBetween(truck.current_location, "4001 South 700 East")
    truck.current_location = "4001 South 700 East"
    print(truck)


# Creates Hash Table
myHash = ChainingHashTable()

truck1 = Truck(16, 18, [], 0, "4001 South 700 East", timedelta(hours=8), timedelta(hours=8))
truck2 = Truck(16, 18, [], 0, "4001 South 700 East", timedelta(hours=9, minutes=5), timedelta(hours=9, minutes=5))
truck3 = Truck(16, 18, [], 0, "4001 South 700 East", timedelta(hours=9, minutes=45), timedelta(hours=9, minutes=45))

# Loads packages into hash table from packageCSV.csv
load_packages('packageCSV.csv')

# Create distance_data list to hold distances
distance_data = []
# Load distances into distance_data array
loadDistanceData(distance_data)

# Create address_data list to hold addresses
address_data = []
# Load addresses into address_data array
loadAddressData(address_data)

truckDeliverPackages(truck1)
truckDeliverPackages(truck2)
truckDeliverPackages(truck3)
