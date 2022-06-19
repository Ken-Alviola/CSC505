pothole_dict = {1: {'Street': 'Hummingbird Lane',
                    'Zip': 78251,
                    'Size': 7,
                    'Location': 'Inner'
                    },
                2: {'Street': 'Marzano Street',
                    'Zip': 78259,
                    'Size': 2,
                    'Location': 'Outer'}
                }

def request_id():
    print('Welcome to the Pothole Tracking and Repair System')
    print('-------------------------------------------------')
    pid = input('Please enter the ID number or press Enter to continue: ')
    print()
    if pid.isdigit() == True:
        pid = int(pid)
    else:
        pid = register_new()
    return pid

def register_new():
    Street = input('Please enter the street: ')
    Zip = int(input('Please enter the Zipcode: '))
    Size = int(input('Enter the size of the pothole (1-10): '))
    Location = input('Enter the location (Inner,Mid,Outer): ')
    print()

    new_id = len(pothole_dict) + 1
    pothole_dict[new_id] = {'Street': Street,
                            'Zip': Zip,
                            'Size': Size,
                            'Location': Location}
    pid = new_id
    return pid

def display_info(pid):
    if pid in list(pothole_dict.keys()):
        print('ID number:',pid)
        for x in pothole_dict[pid]:
            print(x, ':', pothole_dict[pid][x])

    if pothole_dict[pid]['Zip'] <= 78255:
        district = 1
    else:
        district = 2

    if pothole_dict[pid]['Size'] >= 1 and pothole_dict[pid]['Size'] < 5:
        priority = 'Low'
    elif pothole_dict[pid]['Size'] >= 5 and pothole_dict[pid]['Size'] < 8:
        priority = 'Medium'
    elif pothole_dict[pid]['Size'] >= 8:
        priority = 'High'
    
    print()
    print(f'This falls under district: {district}')
    print(f'Current priority is: {priority}')

def run_phtrs():
    pid = request_id()
    display_info(pid)