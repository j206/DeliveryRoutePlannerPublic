import csv


# Linked hash table class with initial capacity 1.3x of the 
# stated average daily package load.
# Complexity: O(n)
class HashTable:
    # Constructor
    # Complexity: 0(1)
    def __init__(self, initial_capacity=53):
        self.table = []
        self.package_count = 0
        for _ in range(initial_capacity):
            self.table.append([])


    # Insert a package into the hash table.
    # Complexity: O(1)
    def insert(self, package):
        bucket = package.package_id % len(self.table)
        bucket_packages = self.table[bucket]

        bucket_packages.append(package)
        self.package_count += 1


    # Select and return a specified package.
    # Complexity: O(n)
    def select(self, key):
        bucket = key % len(self.table)
        bucket_packages = self.table[bucket]

        for p in bucket_packages:
            if p.package_id == key:
                return p
        return print('Package not found\n')


    # Update one specific attribute of a package.
    # Complexity: O(n)
    def update(self, key, value, field='selected_field'):
        bucket = key % len(self.table)
        bucket_packages = self.table[bucket]

        for p in bucket_packages:
            if p.package_id == key:
                if field == 'address':
                    p.address = value
                elif field == 'address_id':
                    p.address_id = value
                elif field == 'city':
                    p.city = value
                elif field == 'state':
                    p.state = value
                elif field == 'zipcode':
                    p.zipcode = value
                elif field == 'deadline':
                    p.deadline = value
                elif field == 'weight':
                    p.weight = value
                elif field == 'requirements':
                    p.requirements = value
                elif field == 'current_location':
                    p.current_location = value
                elif field == 'current_time':
                    p.current_time = value
                elif field == 'status':
                    p.status = value
                elif field == 'loaded_time':
                    p.loaded_time = value
                elif field == 'delivered_time':
                    p.delivered_time = value


    # Remove a package from a hash table.
    # Unused in implementation but included for basic CRUD.
    # Complexity: O(n)
    def delete(self, key):
        bucket = key % len(self.table)
        bucket_packages = self.table[bucket]

        for p in bucket_packages:
            if p.package_id == key:
                bucket_packages.remove(p)
                return print(f'Deleted Package #{key} for {p.address}\n')
        return print('Package not found\n')
