authorized_users = [('Ken', 'StoneFr33'), ]

appcounter_dict = {'Camera': 23,
                   'Stocks': 15,
                   'Mail': 60,
                   'FTX': 20,
                   'Viber': 32,
                   'Messages': 44,
                   'Youtube': 52,
                   'Twitter': 33,
                   'Spotify': 27,
                   'USAA': 24
                   }

def login():
    '''authentication'''
    name, passw = input('Enter your username: '), input('Enter you password: ')
    login = (name.strip(), passw.strip())
    return login

def run_phone():
    '''Function to run the phone app. Menu includes a printout of apps ranked by their usage and an option to choose an app which increases its usage by 1'''
    credentials = login()

    if credentials in authorized_users:
        print()
        print('Welcome',credentials[0])
        menu_selection = 0

        while menu_selection != 3:
            print('-------------------------')
            print('1-Favorite apps\n2-App selection\n3-Exit')
            print('-------------------------')
            menu_selection = int(input('\nType the number of your selection: '))

            if menu_selection == 1:
                print('\nYour favorite apps according to usage:\n')
                sorted_dict = {k: v for k, v in sorted(
                    appcounter_dict.items(), key=lambda item: item[1], reverse=True)}
                count = 0
                for x in sorted_dict:
                    count += 1
                    print(count, x, ':', sorted_dict[x])
                print()

            elif menu_selection == 2:
                print()
                print(sorted(appcounter_dict))
                app_choice = input('\nType the app name of your choosing: ').capitalize()
                if app_choice == 'Ftx' or app_choice == 'FTx' or app_choice == 'FtX':
                    app_choice = 'FTX'
                appcounter_dict[app_choice] += 1

            else:
                menu_selection = 3

    else:
        print('Login Failed')