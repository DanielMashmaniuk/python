def describe_city(name_city,name_country='Ukraine'):
    print(f'\n{name_city.title()} is in {name_country.title()}')
    
describe_city('kiyv')
describe_city('paris',name_country='france')
describe_city('warshawa',name_country='poland')