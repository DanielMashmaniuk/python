chisla = []
chisla = list(range(1, 10))
for chislo in chisla:
    if chislo == 1:
        print(f'{chislo}st')
    elif chislo == 2:
        print(f'{chislo}nd')
    elif chislo == 3:
        print(f'{chislo}rd')
    else :
        print(f'{chislo}th')