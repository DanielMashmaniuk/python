current_users = ['feNix12','Dog54','caT78','kittI13','oNix666']
new_users = ['doG54','cAt78','vii','froG5','piG0']

for current_user in current_users:
    for new_user in new_users:
        if new_user.lower() == current_user.lower() :
            print('Ви маєте обрати інше імя')
        else :
            print('Це імя вільне')