'''
Name: Ben Howell-Burke
Lab 2 
'''

import sys

day_num = int(input('Please enter a number between 1 and 7: '))

day = ''
month = ''

spring = ['Spring', 'spring', 'SPRING']
summer = ['Summer', 'summer', 'SUMMER']
fall = ['Fall', 'fall', 'FALL']
winter = ['Winter', 'winter', 'WINTER']

if day_num == 1:
    day = 'Monday'
elif day_num == 2:
    day = 'Tuesday'
elif day_num == 3:
    day = 'Wednesday'
elif day_num == 4:
    day = 'Thursday'
elif day_num == 5:
    day = 'Friday'
elif day_num == 6:
    day = 'Saturday'
elif day_num == 7:
    day = 'Sunday'
else:
    print('incorrect input terminating program.')
    sys.exit()

season = input('What season is it: ')

if season == spring[0] or season == spring[1] or season == spring[2]:
    month = 'March'
elif season == summer[0] or season == summer[1] or season == summer[2]:
    if day_num <= 3:
        month = 'June'
    else:
        month = 'July'
elif season == fall[0] or season == fall[1] or season == fall[2]:
    month = 'September'
elif season == winter[0] or season == winter[1] or season == winter[2]:
    month = 'December'
else:
    print('incorrect input terminating program.')
    sys.exit()

print(f'The day is {day} which is day number: {day_num}')
print(f'The season is {season} in the month of {month}')

if season.lower() == 'summer':
    if day_num == 6:
        print('Go swimming!')


