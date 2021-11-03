import datetime
import delivery_map
import delivery_operations
import package
import truck
import menu


# Initialize the core package hash table and city map with provided 
# CSV data.
# Complexity: O(n^2) via delivery_map.create_delivery_map
created_delivery_map = delivery_map.create_delivery_map(
    'data/address_data.csv', 'data/distance_data.csv')
all_packages = package.import_package_data(
    'data/package_data.csv', created_delivery_map)

# Create and manually load truck #1.
# Includes primarily packages with non-EOD delivery deadlines.
# Departure time: 8:00AM
# Complexity: O(n^2) via truck.load_packages
truck1_departure_time = datetime.datetime(2021, 1, 1, 8, 0, 0)
truck1_batch1 = [1, 4, 13, 14, 15, 16,
                 19, 20, 21, 29, 30, 31, 34, 37, 39, 40]
truck1 = truck.Truck(1, truck1_departure_time)
truck.load_packages(truck1, all_packages, truck1_batch1, truck1_departure_time)

# Create and manually load truck #2.
# Includes packages delayed by late incoming flights, departs later.
# Departure time: 9:05AM
# Complexity: O(n^2) via truck.load_packages
truck2_departure_time = datetime.datetime(2021, 1, 1, 9, 5, 0)
truck2_batch1 = [2, 3, 5, 6, 12, 17, 18, 22, 25, 26, 28, 32, 33, 36, 38]
truck2 = truck.Truck(2, truck2_departure_time)
truck.load_packages(truck2, all_packages, truck2_batch1, truck2_departure_time)

# Send off trucks #1 and #2 to deliver their packages.
# Complexity: o(n^2) via delivery_operations.deliver_packages
truck1_end_time = delivery_operations.deliver_packages(
    truck1, created_delivery_map, all_packages)
truck2_end_time = delivery_operations.deliver_packages(
    truck2, created_delivery_map, all_packages)

# Create and manually load truck #3.
# Includes package (#9) with incorrect address.
# Mistake is corrected at 10:20AM.
# Departure time: 10:20AM (Truck 1 returned at 10:16:40AM using this data set)
# Complexity: O(n^2) via truck.load_packages
truck3_departure_time = datetime.datetime(2021, 1, 1, 10, 20, 0)
truck3_batch1 = [7, 8, 9, 10, 11, 23, 24, 27, 35]
truck3 = truck.Truck(3, truck3_departure_time)
truck.load_packages(truck3, all_packages, truck3_batch1, truck3_departure_time)

# Fix the incorrect information for package #9.
# Complexity: O(n) via HashTable.update
all_packages.update(9, '410 S State St', 'address')
all_packages.update(9, 19, 'address_id')
all_packages.update(9, '84111', 'zipcode')
truck3_departure_time = truck1_end_time

# Send off truck #3.
# Complexity: (n^2) via delivery_operations.deliver_packages
truck3_end_time = delivery_operations.deliver_packages(
    truck3, created_delivery_map, all_packages)

# Calculate EOD truck mileage.
# Complexity: O(1)
total_day_mileage = truck1.total_mileage + \
    truck2.total_mileage + truck3.total_mileage

# Display user interface.
# Complexity: O(n^2) via menu.display_menu
menu.display_menu(all_packages, total_day_mileage)