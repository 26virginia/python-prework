#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odd():
    for num in range(1,101):
        if num % 2 != 0:
            print(num)
first_odd()