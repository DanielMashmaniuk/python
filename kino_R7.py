kino = 'Введіть свій вік :'
age = ''

while kino != 'break':
    age = int(input(kino))
    if age <= 3 :
        print('у вас безкоштовний квииок')
        break
    elif 3<age<=12:
        print('Ваш квиток коштує 10$')
        break
    else:
       print('Ваш квитрк коштує 15$') 
       break
        