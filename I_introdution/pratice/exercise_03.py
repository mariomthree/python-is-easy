age = int(input('Age: '))
gender = input('Genger[M/F]: ')
gender = gender.upper()
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif 18 <= age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')