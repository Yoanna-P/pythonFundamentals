# Integer operations
'''
first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

result = int((first + second)/third) * fourth
print(result)

# Chars to String

first = input()
second = input()
third = input()

result = first + second + third
print(result)


# Elevator

n = int(input())
p = int(input())

if n%p == 0:
    print(int(n/p))
else:
    print(int(n/p+1))

# Elevator - vtori nachin

n = int(input())
p = int(input())

import math

print(math.ceil(n/p))

# Sum of Chars

n = int(input()) #number of lines
sum = 0

for i in range(1, n+1):
    char = input()
    sum += ord(char)
    char =""
print(f"The sum equals: {sum}")

# Print part of the ASCII table

first = int(input())
last = int(input())

for i in range(first, last+1):
    print(chr(i), end=" ")


#Triples of latin letters

n = int(input())

for i in range(1, n+1):
    for k in range(1, n+1):
        for j in range(1, n+1):
            print(f"{chr(i+96)}{chr(k+96)}{chr(j+96)}")


# Water overflow

capacity = 255
n = int(input())
current_sum = 0
old_sum = 0

for i in range(1, n+1):
    l = int(input())
    current_sum += l
    if current_sum > 255:
        print("Insufficient capacity!")
        current_sum = old_sum
    else:
        old_sum += l
print(old_sum)


# 8. Party Profit

comp = int(input())
days = int(input())
coins = 0

for i in range(1, days+1):
    if i%10 == 0:
        comp -= 2
    if i%15 == 0:
        comp += 5
    coins += 50 - 2*comp
    if i%3 == 0:
        coins -= 3*comp
    if i%5 == 0:
        coins += 20*comp
        if i%3 == 0:
            coins -= 2*comp

print(f"{comp} companions received {int(coins/comp)} coins each.")


# 9. Snowballs

n = int(input()) # number of snowballs made by them
max = 0

for i in range(1, n+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = pow((snowball_snow/snowball_time), snowball_quality)
    if value > max:
        max = value
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_snow} : {best_time} = {int(max)} ({best_quality})")

'''

# 10. Gladiators

count = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shield_count = 0

for i in range(1, count+1):
    if i%2==0:
        expenses += helmet
    if i%3==0:
        expenses += sword
        if i%2 == 0:
            expenses += shield
            shield_count += 1
            if shield_count%2 == 0:
                expenses += armor
print(f"Gladiator expenses: {expenses:.2f} aureus")














