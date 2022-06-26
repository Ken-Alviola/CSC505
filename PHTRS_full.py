import pandas as pd 

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



workorder_df = pd.DataFrame(columns=['Pothole_ID',
                                     'Location',
                                     'Size',
                                     'Crew_ID',
                                     'Crew_size',
                                     'Repair_hours',
                                     'Repair_status',
                                     'Filler_amount(cu_ft)',
                                     'Repair_cost'])

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

def welcome(damage_df):
    print('Welcome to the PHTRS main page. Choose an option to continue')
    print('---------------------------------------')
    selection = ''
    while selection != 'q':
        print()
        print('Type 1 to view or register a new repair.')
        print('Type 2 to report damages')
        print('Type 3 for admin functions')
        print('Type q to exit')
        selection = input('Your selection: ')
        if selection == '1':
            print()
            run_phtrs()
            print()
        elif selection == '2':
            print()
            damage_df = damage_report(damage_df)
            print()
        elif selection == '3':
            print()
            admin(damage_df)
    return damage_df

def damage_report(damage_df):
    name = input('Enter your first and last name: ')
    address = input('Enter your street address and zipcode: ')
    phone = input('Enter your phone number: ')
    damage_type = input('Enter a brief description of the damage: ')
    dollar_amount = input('Enter the approximate dollar amount: ')

    damage_df = damage_df.append({'Name': name,
                                  'Address': address,
                                  'Phone#': phone,
                                  'Type_of_Damage': damage_type,
                                  'Dollar_Amount': dollar_amount},
                                 ignore_index=True)

    return damage_df

def admin(damage_df):
    pothole_df = pd.DataFrame(pothole_dict).T
    select = ''
    while select != 'q':
        select = input(
            'Type 1 to check reported potholes, 2 for workorders, 3 for damage report, and q to quit: ')
        if select == '1':

            print(pothole_df)
            print()
            pid = int(input('Enter the ID to check district and priority: '))
            display_info(pid)
        elif select == '2':
            workorder_df = workorder(pothole_df)
            print()
            print(workorder_df)
            print()
            change = input(
                '''Would you like to change the status of a repair?:
                (functionality will be added in a future update)''')
        elif select == '3':
            print()
            print(damage_df)
            
def crew(size):
    if size < 5:
        return 1
    elif size >= 5 and size < 8:
        return 2
    elif size >= 8:
        return 3
    
def crewsize(crew_id):
    if crew_id == 1:
        return 3
    elif crew_id == 2:
        return 5
    elif crew_id == 3:
        return 7

def repair_hours(size):
    if size < 5:
        return 2
    elif size >= 5 and size < 8:
        return 3
    elif size >= 8:
        return 4

def filler_amount(size):
    if size < 5:
        return 3
    elif size >= 5 and size < 8:
        return 5
    elif size >= 8:
        return 7

def workorder(pothole_df):
    workorder_df['Pothole_ID'] = pothole_df.index.tolist()
    workorder_df['Location'] = pothole_df.Location.tolist()
    workorder_df['Size'] = pothole_df.Size.tolist()
    workorder_df['Crew_ID'] = workorder_df.Size.apply(lambda x: crew(x))
    workorder_df['Crew_size'] = workorder_df.Crew_ID.apply(
        lambda x: crewsize(x))
    workorder_df['Repair_hours'] = workorder_df.Size.apply(
        lambda x: repair_hours(x))
    workorder_df['Repair_status'] = 'not repaired'
    workorder_df['Filler_amount(cu_ft)'] = workorder_df.Size.apply(
        lambda x: filler_amount(x))
    workorder_df['Repair_cost'] = (workorder_df['Repair_hours'] * workorder_df['Crew_size']
                                   * 20) + (workorder_df['Filler_amount(cu_ft)'] * 500)
    
    return workorder_df