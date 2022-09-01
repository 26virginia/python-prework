#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif(a_year % 100 == 0):
        return False
    elif(a_year % 4 == 0):
        return True
    else:
        return False

a_year = int(input("Enter Year: "))
print(is_leap_year(a_year))