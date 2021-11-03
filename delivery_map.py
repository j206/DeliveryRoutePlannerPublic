import csv


# Helper function to read addresses and their corresponding names from 
# CSV file and add to a base dictionary.
# Complexity: O(n)
def import_addresses(address_data):
    addresses = {}
    address_id = 0

    with open(address_data, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            addresses[address_id] = {
                'location_name': row['location_name'],
                'address': row['address']
            }
            address_id += 1
    return addresses


# Helper function to read distances from CSV file and add to a list.
# Complexity: O(n^2)
def import_distances(distance_data):
    distances = []

    with open(distance_data, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            location_distances = []
            for distance in row:
                location_distances.append(float(distance))
            distances.append(location_distances)
    return distances


# Nest the each list of relative distances into the address
# dictionary, rename to delivery_map.
# Complexity: O(n^2) via import_distances
def create_delivery_map(address_data, distance_data):
    addresses = import_addresses(address_data)
    distances = import_distances(distance_data)
    address_id_index = 0

    for address in addresses:
        addresses[address]['distances'] = distances[address_id_index]
        address_id_index += 1
    delivery_map = addresses
    return delivery_map


# Helper function to return a location's integer ID number 
# from its address.
# Complexity: O(n)
def get_location_id(created_delivery_map, address):
    if address == 'HUB':
        return 0
    else:
        for location_id in created_delivery_map:
            formatted_address = created_delivery_map[location_id]['address'][:-8]
            if formatted_address == address:
                return location_id
    return print(f'Couldn\'t find address {address}')
