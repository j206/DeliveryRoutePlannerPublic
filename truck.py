import hashtable


class Truck:
    # Constructor
    # Complexity: 0(1)
    def __init__(self, truck_id, departure_time):
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.max_capacity = 16
        self.speed_mph = 18
        self.loaded_packages = []
        self.visited_locations = [0]
        self.current_location = 0
        self.total_mileage = 0


# Load a subset of all packages onto a specific truck and 
# update the status of those packages.
# Complexity: O(n^2) via HashTable.update
def load_packages(truck, all_packages, batch_manifest,  current_time):
    for package_id in batch_manifest:
        truck.loaded_packages.append(all_packages.select(package_id))
        all_packages.update(package_id, current_time, 'current_time')
        all_packages.update(package_id, current_time, 'loaded_time')
        all_packages.update(package_id, 'ON TRUCK', 'status')


# Calculate the amount of time to get from a truck's current 
# location to the next.
# Complexity: O(1)
def get_travel_time(truck, distance_to_next):
    travel_time_min = distance_to_next / (truck.speed_mph / 60 )
    travel_time_sec = round(travel_time_min * 60, 0)
    return travel_time_sec
