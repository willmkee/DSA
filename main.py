from Package import Package
from Truck import Truck
import csv
from HashTable import ChainingHashTable
from utils import load_packages, loadDistanceData, loadAddressData

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

truck1.add_package(myHash.search(1))
truck1.add_package(myHash.search(2))
print(truck1)