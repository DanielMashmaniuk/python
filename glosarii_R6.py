contents = {
    'del': 'Видаляє всі значення назажди',
    'upper()': 'Метод який робить всі букви великими',
    'lower()': 'Метод який робить всі букви маленькими',
    'title()': 'Метод який робить заглавну букву великою',
    'remove()': 'Метод який видаляє з можливістю далі працювати з тим елементом',
    'get()': 'перевіряє чи є значення в словнику',
    '**' : 'Піднесення до степеня в мові python',
    '==' : '',
    '=!': '',
    }
new_contents = { 'title()','get()','==','=!'}
# for key,value in contents.items():
#     if key not in new_contents:
#         print(f'\n{key}: \n{value}  ')
#     else:
#         print(f'\nkey: \nThis content dont found')
for content in contents.keys() :
    print(content)
    if content not in new_contents:
        print(f'\t{content} is founded')
    else :
        print(f'\t{content} not founded')