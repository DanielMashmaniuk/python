message = ('Введіть назву піци :')
active = True

while active:   
    piza = input(message)
    if piza == 'quit':
        print('Game ower')
        active= False
    else:
        print(f'Our pizz added ({piza})')