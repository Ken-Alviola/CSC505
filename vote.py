#constructors for initializing userlist, specs, and voting tally
authorized_list = [('admin', '1234'),
                   ('user1','oak'),
                   ('user2','hickory'),
                   ('user3','mesquite')]

spec_dict = {1:'50fps',
            2: '60fps',
            3: '120fps'}

vote_list = [1,1,3]

#Import this .py script then use run_vote() function to use

def login():
    '''authentication'''
    name, passw = input('Enter your username: '), input('Enter you password: ')
    login = (name.strip(), passw.strip())
    return login

def add_spec():
    '''adds user spec to spec_dict'''
    new_spec = False
    add_spec = input('Do you wish to add a specification for voting? Type(y/n): ')
    if add_spec == 'y' or add_spec == 'Y':
        new_spec = input('Input new spec: ')
        return new_spec
    else:
        return False

def vote(credentials):
    '''main vote function, admin can only add spec or view current vote count'''
    if credentials in authorized_list:
        new_spec = add_spec()
        if new_spec != False:
            spec_dict[len(spec_dict)+1] = new_spec
            
        print()
        print(spec_dict,'\n')    
        
        if credentials[0] != 'admin':
            vote = int(input('Type the number of the spec to cast your vote: '))
            vote_list.append(vote)
            print()
            print(f'You voted for spec {vote}: {spec_dict[vote]}')
            print('Thank you. Results will be announced in 48hrs')
        
        if credentials[0] == 'admin':
            print('Current vote count: ')
            count = 1
            while count <= max(vote_list):
                print(spec_dict[count],':',vote_list.count(count),'votes')
                count += 1
        
    else:
        print('Unauthorized user')
        
def run_vote():
    '''Run constructor to initialize lists and dictionary then use run_vote()'''
    credentials = login()
    vote(credentials)
