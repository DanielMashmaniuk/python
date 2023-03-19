name_users = ['Anna','victor', 'DANIEL','maks','admin']
if name_users:
    for name_user in name_users:
        name_user.lower()
        if name_user == 'admin':
            print(f'Hello {name_user.title()} would you like to see a status report')
        else :
            print(f'Hello {name_user.title()}, thank you for loggin in again')
else:
    print('We need to find some users')