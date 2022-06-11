trait_dict = {1: 'Individual Responsibility',
              2: 'Acute Awareness',
              3: 'Brutal Honesty',
              4: 'Resilience under pressure',
              5: 'Sense of Fairness',
              6: 'Attention to detail',
              7: 'Pragmatism'
              }

# preset
trait_counterdict = {'Individual Responsibility': 2,
                     'Acute Awareness': 1,
                     'Brutal Honesty': 3,
                     'Resilience under pressure': 1,
                     'Sense of Fairness': 2,
                     'Attention to detail': 4,
                     'Pragmatism': 2
                     }

def sort_and_rank():
    sorted_dict = {k: v for k, v in sorted(
        trait_counterdict.items(), key=lambda item: item[1], reverse=True)}
    count = 0
    print('Current Ranking:')
    print('-----------------------------------')
    for x in sorted_dict:
        count += 1
        print(count, x, ':', sorted_dict[x])
    print()
    
def choices():
    print('These are Pressman & Maxim\'s (2020) 7 characteristics of a \"superprofessional\" developer: ')
    print('-----------------------------------')
    for x in trait_dict:
        print(x, trait_dict[x])

    print()
    print('*Choose your top 3 characteristics: ')
    print('-----------------------------------')

    choice_num1 = int(input('Input the number of your 1st selection: '))
    choice_num2 = int(input('Input the number of your 2nd selection: '))
    choice_num3 = int(input('Input the number of your 3rd selection: '))

    trait_counterdict[trait_dict[choice_num1]] += 1
    trait_counterdict[trait_dict[choice_num2]] += 1
    trait_counterdict[trait_dict[choice_num3]] += 1

    print()
    print(
        f'You chose: {trait_dict[choice_num1]}, {trait_dict[choice_num2]},and {trait_dict[choice_num3]}.')
    print()
    
def survey():
    '''Run this function from a new instance'''
    choices()
    sort_and_rank()