#!/usr/bin/env python3
'''
as04
ciaran farley
cs-12p spring 2022 cabrillo college
https://jeff.cis.cabrillo.edu/classes/cs12ps22/assignments/assignment_04
'''

import sys
import re

# get the number of bedrooms from user
print('num bedrooms: ', end=' ', file=sys.stderr)
num_bedrooms = input()

# test for num bedrooms not a number
if num_bedrooms.isnumeric() is False:
  print('that is not a number', file=sys.stderr)
  sys.exit(2)

# test for more than 2 bedrooms
elif int(num_bedrooms) > 2:
  print('max bedrooms is 2', file=sys.stderr)
  sys.exit(3)

else:

  # get wage from user
  print('hourly wage: ', end='', file=sys.stderr)
  hourly_wage = input()

  # check for valid input
  if re.match(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', hourly_wage) is None:
    print('not a valid numeric wage', file=sys.stderr)
    sys.exit(4)

  # checkvalid input wage positive
  elif float(hourly_wage) <= 0:
    print('wage must be positive', file=sys.stderr)
    sys.exit(5)

  else:
    # FMR bedrooms information
    # Stolen from Lhea Aragon
    monthly_housing_cost = float(0)

    if int(num_bedrooms) == 0:
      monthly_housing_cost = 2085

    elif int(num_bedrooms) == 1:
      monthly_housing_cost = 2385

    elif int(num_bedrooms) == 2:
      monthly_housing_cost = 3138

    else:
      print('ERROR', file=sys.stderr)


# 40h per week device by 7 days per week gives me hours per day average
hours_per_day = 40 / 7

# hours per day multiply by constant from jeff is hours per month
hours_per_month = hours_per_day * 30.4375

# take monthly housing cost and devide by 33% to make it 30 percent of income
minimum_monthly_wage = monthly_housing_cost / 0.30

# minimum monthly wage devide by hours per month gives you an hourly wage
minimum_hourly_wage = minimum_monthly_wage / hours_per_month

difference = float(hourly_wage) - float(minimum_hourly_wage)


print(f'${float(hourly_wage):.2f}/hr', end='')
print(' is ', end='')
print(f'${abs(float(difference)):.2f}/hr', end='')
if float(difference) > 0:
  print(' greater than ', end='')
elif float(difference) < 0:
  print(' less than ', end='')
elif float(difference) == 0:
  print(' the same as ', end='')
else:
  print('bad input')

print('the housing wage of ', end='')
print(f'${float(minimum_hourly_wage):.2f}/hr')

if float(difference) >= 0:
  sys.exit(0)
else:
  sys.exit(1)
