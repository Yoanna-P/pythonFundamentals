# 1. concat names
'''
first = input()
second = input()
middle = input()

print(f"{first}{middle}{second}")


#2.Centuries to Minutes

cen = int(input())
years = int(cen*100)
days = int(years * 365.2422)
hours = days*24
minutes = hours * 60

print(f'{cen} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
# 3.Special numbers - sum if its digits is 5, 7 or 11

num = int(input())
sum_digits = 0

for i in range(1, num+1):
    for digit in str(i):
        sum_digits += int(digit)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
    sum_digits = 0

'''

