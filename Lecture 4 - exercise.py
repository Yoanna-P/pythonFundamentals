'''
# 1.Smallest of Three

def smallest_num(a, b, c):
    return min(a, b, c)

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_num(num1, num2, num3))

# 2. Add and Subtract

num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(a, b):
    res = a + b
    return res

def subtract(c, d):
    res1 = c - d
    return res1

def add_and_subtract(a, b, c):
    sum_numbers(a, b)
    res2 = subtract(a+b, c)
    return res2

print(add_and_subtract(num1, num2, num3))



# 3. Characters in Range

char1 = input()
char2 = input()

def char_between(a, b):
    for i in range(ord(a)+1, ord(b)):
        print(chr(i), end=" ")

char_between(char1, char2)

for i in range(len(number)):
    number[i] = int(number[i])
    if not number[i]%2 == 0:
        odd_sum+=number[i]
    else:
        even_sum+=number[i]



# 4. Odd and Even Sum - works, but this is without a function

number = int(input())
odd_sum=0
even_sum=0

for char in number:
    char = int(char)
    if char%2==0:
        even_sum += char
    else:
        odd_sum += char

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

# could not make it work with a function

num = int(input())
odd_sum=0
even_sum=0

def odd_even_sum(number):
    number = str(number)
    for char in number:
        char = int(char)
        if char % 2 == 0:
            even_sum += char
            return even_sum
        else:
            odd_sum += char
            return odd_sum

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

# 5. Palindrome Integers

num_list = input().split(", ")
for num in num_list:
    if num == num[::-1]:
        print("True")
    else:
        print("False")

# with a function:

def palindrome(list_num):
    num_list = list_num.split(", ")
    for num in num_list:
        if num == num[::-1]:
            print("True")
        else:
            print("False")

numbers = input()
palindrome(numbers)

# from Ines:


def is_palindrome(el):
    if el == el[::-1]:
        return True
    return False

numbers = input().split(", ")

for num in numbers:
    print(is_palindrome(num))

6. Password validator

password = input()
num_digits = 0

for char in password:
    if char.isdigit():
        num_digits +=1

if not 6 <= len(password) <= 10:
    print("Password must be between 6 and 10 characters")
if not password.isalnum():
    print("Password must consist only of letters and digits")
if num_digits < 2:
    print("Password must have at least 2 digits")
else:
    print("Password is valid")


#6. Password validator with a function:

user_pw = input()

def validator(password):
    num_digits = 0
    for char in password:
        if char.isdigit():
            num_digits += 1

    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    if num_digits < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")

validator(user_pw)

# 7. Perfect number with a while loop

num = int(input())
i = 1
sum_divisors = 0

while i < num:
    if num%i == 0:
        sum_divisors += i
    i+=1

if sum_divisors == num:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")




8. Loading Bar

num = int(input())

a = num//10

if a == 10:
    print("100% Complete!")
    print(f"[{10 * '%'}]")
else:
    print(f"{a * 10}% [{a * '%'}{(10 - a) * '.'}]")
    print("Still loading...")

# 8. Loading Bar with a function

number = int(input())

def loading_bar(num):

    a = num // 10

    if a == 10:
        print("100% Complete!")
        print(f"[{10 * '%'}]")
    else:
        print(f"{a * 10}% [{a * '%'}{(10 - a) * '.'}]")
        print("Still loading...")

loading_bar(number)

# 9.

num1 = int(input())
num2 = int(input())

factorial1 = 1
factorial2 = 1

for i in range(1, num1+1):
    factorial1 = i*factorial1
for j in range(1, num2+1):
    factorial2 = j*factorial2

print(f"{factorial1/factorial2:.2f}")

# with a 2-argument- function:

number1 = int(input())
number2 = int(input())

def factor(num1, num2):
    factorial1 = 1
    factorial2 = 1

    for i in range(1, num1 + 1):
        factorial1 = i * factorial1
    for j in range(1, num2 + 1):
        factorial2 = j * factorial2

    print(f"{factorial1 / factorial2:.2f}")


factor(number1, number2)


# with a 1-argument-function

def calc_factorial(num):
    factorial_total = 1
    for i in range(1, num+1):
        factorial_total *= i
    return factorial_total


number1 = int(input())
fact_number1 = calc_factorial(number1)

print(calc_factorial(number1))


# 6. Password validator

password = input()
num_digits = 0

for char in password:
    if char.isdigit():
        num_digits +=1

if not 6 <= len(password) <= 10:
    print("Password must be between 6 and 10 characters")
if not password.isalnum():
    print("Password must consist only of letters and digits")
if num_digits < 2:
    print("Password must have at least 2 digits")
else:
    print("Password is valid")


#6. Password validator with a function:

user_pw = input()

def validator(password):
    num_digits = 0
    for char in password:
        if char.isdigit():
            num_digits += 1

    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    if num_digits < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")

validator(user_pw)

'''

# 7 with a function and a for loop

number = int(input())


def perfect_num(num):

    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        return True
    return False


if perfect_num(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
