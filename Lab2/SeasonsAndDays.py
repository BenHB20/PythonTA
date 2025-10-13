#import sys to use the .exit() method to close the code instantly 
import sys

# ask for user input for the day and cast it to an integer 
day_num = int(input('Please enter a number between 1 and 7: '))

# create variables holding empty strings to hold information later on
day = ''
month = ''

#create lists with different phrasing of the naming convention for each season 
spring = ['Spring', 'spring', 'SPRING']
summer = ['Summer', 'summer', 'SUMMER']
fall = ['Fall', 'fall', 'FALL']
winter = ['Winter', 'winter', 'WINTER']

#conditionals for what day it is 
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


#ask the user for what season it is 
season = input('What season is it: ')

#conditionals for what season it is with an inbedded conditional statement for summer. 
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


#final print statement and conditionals for the lab in which I used an f string to directly input the variables into the prints
print(f'The day is {day} which is day number: {day_num}')
print(f'The season is {season} in the month of {month}')

# final conditional which uses the .lower() function to turn the user input to a completely lower case string. 
if season.lower() == 'summer':
    if day_num == 6:
        print('Go swimming!')


