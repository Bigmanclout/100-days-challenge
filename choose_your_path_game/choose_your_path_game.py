user_name = input('WHAT IS YOUR NAME? ')
print(f'welcome {user_name} to this adventure')


answer = input('which way would you have to go?(left/right) ').lower()
if answer == 'left':
    answer = input('go to a gay orgy party or spend the night with diddy? (gay/ night with diddy)').lower()
    if 'gay' in answer:
        print('you have a black dudes slug in you')
    elif 'night' or 'diddy' in answer:
        print('you got molested by diddy')
    else:
        print('invalid option')
elif answer == 'right':
    pass
else:
    print('not a valid option')
