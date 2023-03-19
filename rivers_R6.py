rivers = {
    'dnipro': 'ukraine',
    'amazonka':'brazilia',
    'nile':'egypt',
    }

for key,value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}')
print('Rivers:')
for river in rivers.keys():
    print(f'\t{river.title()}')
print(f'Countrys:')
for country in rivers.values():
    print(f'\t{country.title()}')