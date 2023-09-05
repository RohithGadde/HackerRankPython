def is_leap(year):

    # variable to check the leap year
    leap = False

    if (year % 400 == 0) and (year % 100 == 0):

       # change leap to True
        leap = True

    elif (year % 4 == 0) and (year % 100 != 0):

        # Change leap to true
        leap = True

    # else not a leap year
    else:
        pass

    return leap
