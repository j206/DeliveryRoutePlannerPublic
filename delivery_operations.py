import truck
import delivery_map
import hashtable
import datetime
from truck import get_travel_time


# Find the "nearest neighbor" for a truck based on its current location.
# Returns a list of the ID of the next destination, and the distance in
# miles to get there.
# Complexity: O(n)
def find_nearest_location(truck, created_delivery_map):
    potential_locations = []
    shortest_location_id = 0
    shortest_distance = 100

    for loaded_package in truck.loaded_packages:
        potential_locations.append(loaded_package.address_id)

    # Loop through the potential locations' IDs, access the index of
    # the truck's current location in the list of relative distances,
    # and determine the smallest non-zero distance.
    for location_id in potential_locations:
        distance_to_location = created_delivery_map[location_id]['distances'][truck.current_location]
        if 0 < distance_to_location < shortest_distance:
            shortest_location_id = location_id
            shortest_distance = distance_to_location

    return [shortest_location_id, shortest_distance]


# Handle the core of a single truck's delivery behavior (time
# advancement, routing, mileage, and package status).
# Return the return time of the truck.
# Complexity: O(n^2)
def deliver_packages(truck, created_delivery_map, all_packages):
    trip_mileage = 0
    current_time = truck.departure_time
    
    # Deliver packages as long as the truck isn't empty.
    while len(truck.loaded_packages) > 0:
        nearest_location = find_nearest_location(truck, created_delivery_map)
        next_location_id = nearest_location[0]
        distance_to_next = nearest_location[1]

        time_to_next_sec = get_travel_time(truck, distance_to_next)
        current_time += datetime.timedelta(seconds=time_to_next_sec)

        # Move the truck to the next location.
        truck.current_location = next_location_id
        trip_mileage += distance_to_next

        # Deliver packages at the current location.
        for loaded_package in truck.loaded_packages:
            if loaded_package.address_id == truck.current_location:
                all_packages.update(
                    loaded_package.package_id, 'DELIVERED', 'status')
                all_packages.update(loaded_package.package_id,
                                    current_time, 'delivered_time')

        for loaded_package in truck.loaded_packages:
            if loaded_package.status == 'DELIVERED':
                truck.loaded_packages.remove(loaded_package)

    next_location_id = 0
    distance_to_hub = created_delivery_map[truck.current_location]['distances'][0]
    time_to_hub_sec = get_travel_time(truck, distance_to_hub)

    trip_mileage += distance_to_hub
    truck.total_mileage = trip_mileage

    current_time += datetime.timedelta(seconds=time_to_hub_sec)
    return current_time