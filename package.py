import csv
import delivery_map
from hashtable import HashTable


class Package:
    # Constructor
    # Complexity: 0(1)
    def __init__(self, package_id, address, address_id, city, state, zipcode, deadline, weight, requirements):
        self.package_id = int(package_id)
        self.address = address
        self.address_id = address_id
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.requirements = requirements
        self.current_time = None
        self.status = 'HUB'
        self.loaded_time = None
        self.delivered_time = None


# Create a new hash table from provided CSV package data.
# Complexity: O(n^2) via HashTable.insert
def import_package_data(package_data, created_delivery_map):
    all_packages = HashTable()

    with open(package_data, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            package_id = row[0]
            address = row[1]
            address_id = delivery_map.get_location_id(
                created_delivery_map, address)
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            requirements = row[7]

            new_package = Package(package_id, address, address_id, city,
                                  state, zipcode, deadline, weight, requirements)
            all_packages.insert(new_package)
    return all_packages
