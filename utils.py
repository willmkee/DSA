# Distance method for addresses
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
    return distance

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
            package_status = "At Hub"

            # Creates new package object
            p = Package(package_id, package_address, package_city, package_state,
                        package_zip, package_deadline, package_weight, package_status)

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