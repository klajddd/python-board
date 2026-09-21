
def is_leap(year):
    leap = False

    # Write your logic here
    '''
    The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100 then it is NOT a leap year, unless:5
    The year is also evenly divisible by 400. Then it is a leap year.
    '''
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False

    return leap


year = int(input("enter year: \n"))
print(is_leap(year))
