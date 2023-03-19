responses = {}

polling_active = True

while polling_active:
    name = input('\nВведіть своє імя ')
    response = input('В яке місце ви б хотіли поїхати у відпустку ')
    
    responses[name] = response
    repeat = input('Ще хтось буде проходити опитування? yes or no ')
    if repeat == 'no':
        polling_active = False
print('------Poll results------')
for name,response in responses.items():
    print(f'{name} хотів би поїхати на вудпустку у: {response}')
    