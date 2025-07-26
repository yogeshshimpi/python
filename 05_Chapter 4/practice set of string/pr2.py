# 2. Write a program to fill in a letter template given below with name and date.
# letter ='''
#           Dear <Name>,
#           You are selected!
#           </Date|>
#         '''


name = input('Enter your name: ')

date = int(input('Enter you birth date: '))
month = int(input('Enter you birth month: '))
year = int(input('Enter you birth year: '))

date = f'{date}/{month}/{year}'

letter = f'''
          Dear {name},
          You are selected!
          {date}
        '''
        
print(letter)


# Output:
#     Enter your name: John Cena
#     Enter you birth date: 23
#     Enter you birth month: 4
#     Enter you birth year: 1977
# 
#           Dear John Cena,
#           You are selected!
#           23/4/1977
