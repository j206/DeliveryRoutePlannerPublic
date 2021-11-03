import hashtable
import datetime

# Display the header and present the main menu options.
# Complexity: O(n^2) via handle_user_input
def display_menu(all_packages, total_day_mileage):
    print_header()
    handle_user_input(all_packages, total_day_mileage)


# Handle the selection of main menu options.
# Complexity: O(n^2) via print_all_eod_status, print_status_at_time
def handle_user_input(all_packages, total_day_mileage):
    selected_option = ''
    while selected_option != '3':
        print_options()
        selected_option = input('Please select an option: ').strip()
        print()
        if selected_option == '1':
            print_all_eod_status(all_packages, total_day_mileage)
        elif selected_option == '2':
            print_status_at_time(all_packages)
        elif selected_option == '3':
            print('Quitting application...')
            print()
            exit()
        else:
            print('Invalid option.')


# Option #1: Print EOD and total truck mileage.
# Complexity: O(n^2)
def print_all_eod_status(all_packages, total_day_mileage):
    print('Displaying information for all packages at end-of-day...')
    print_column_headers()
    for p in range(1, all_packages.package_count + 1):
        package = all_packages.select(p)
        delivered_time = package.delivered_time.time()
        print('{:<3} | {:<40} | {:<16} | {:<6} | {:<5} | {:<11} | {:<3} | DELIVERED at {}'.format(
            package.package_id, package.address, package.city, package.state, package.zipcode,
            package.deadline, package.weight, delivered_time))
    print()
    print(f'Total miles traveled by trucks: {total_day_mileage}')


# Option #2: Print specific time status.
# Complexity: O(n^2)
def print_status_at_time(all_packages):
    validated_time = None
    while validated_time == None:
        print('Enter a time below to view the status of all packages at that time.')
        print('Please format desired time as HH:MM:SS in 24-hour format.')
        selected_time = input('Time: ')
        print()
        validated_time = validate_user_time(selected_time)

    formatted_time = validated_time.strftime('%H:%M:%S')
    print(f'Displaying information for all packages at {formatted_time}...')
    print_column_headers()

    # Complexity: O(n^2)
    for p in range(1, all_packages.package_count + 1):
        package = all_packages.select(p)
        delivered_time = package.delivered_time.time()
        loaded_time = package.loaded_time.time()

        if validated_time > delivered_time:
            print('{:<3} | {:<40} | {:<16} | {:<6} | {:<5} | {:<11} | {:<3} | DELIVERED at {}'.format(
                package.package_id, package.address, package.city, package.state, package.zipcode,
                package.deadline, package.weight, delivered_time))
        elif validated_time > loaded_time:
            print('{:<3} | {:<40} | {:<16} | {:<6} | {:<5} | {:<11} | {:<3} | ON TRUCK'.format(
                package.package_id, package.address, package.city, package.state, package.zipcode,
                package.deadline, package.weight))
        else:
            print('{:<3} | {:<40} | {:<16} | {:<6} | {:<5} | {:<11} | {:<3} | NOT LOADED'.format(
                package.package_id, package.address, package.city, package.state, package.zipcode,
                package.deadline, package.weight))
    return


# Validate that the user entered a properly formatted time.
# Complexity: O(1)
def validate_user_time(selected_time):
    time_format = '%H:%M:%S'
    try:
        validated_time = datetime.datetime.strptime(selected_time, time_format)
        return validated_time.time()
    except ValueError:
        print('Invalid time')
        return None


# Complexity: O(1)
def print_header():
    print(' Delivery Management System')


# Complexity: O(1)
def print_options():
    print('''
    Options:
        1. View package status at end-of-day & Total truck mileage
        2. View package status at specific time
        3. Quit
    ''')


# Complexity: O(1)
def print_column_headers():
    print('{:<3} | {:<40} | {:<16} | {:<6} | {:<5} | {:<11} | {:<3} | {:<20}'.format(
        'ID:', 'ADDRESS:', 'CITY:', 'STATE:', 'ZIP:', 'DELIVER BY:', 'KG:', 'STATUS:'))
