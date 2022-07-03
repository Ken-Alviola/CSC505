pin = 4550
checking = 2500
authorized = False
pin_counter = 0

def read_pin(pin,authorized,pin_counter):
    print('Reading card..........')
    print()
    print('Welcome to NSolvent Bank')
    print('------------------------')
    while authorized == False and pin_counter < 4:
        pin_check = int(input('Please enter your PIN: '))
        if pin_check == pin:
            authorized = True
        else:
            print('Incorrect Pin')
            print()
            pin_counter += 1

    if pin_counter >= 4:
        authorized == False
        return authorized
    else:
        return authorized
    
def choose_transaction(checking):
    selection = ''
    while selection != 'q':
        selection = input('Input 1 to check balance, 2 to withdraw cash, q to quit: ')
        if selection == '1':
            print(f'Checking balance: ${checking}')
            print()
        elif selection == '2' and checking > 0:
            withdraw_amount = int(input('Type an amount to withdraw: '))
            if withdraw_amount <= checking:
                checking = checking - withdraw_amount
                print(f'New balance: ${checking}')
                print()
            else:
                print('Invalid withdrawal amount.')
                print()
        elif checking == 0:
            print('Warning! Your account balance is 0 and will be closed in 14 days.')
            print()
        
    print('Complete. Please take your card')
    return checking

def run_atm(pin, authorized, pin_counter, checking):
    authorized = read_pin(pin,authorized,pin_counter)
    if authorized == True:
        checking = choose_transaction(checking)
    else:
        print('Card Rejected.')
    return checking