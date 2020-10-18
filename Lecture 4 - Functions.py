'''
#2. Calculations

input_operator = input()
first_num = int(input())
second_num = int(input())

def calculator(num1, num2, operator="multiply"):
    result = None
    if operator == "multiply":
        result = num1*num2
    elif operator == "divide":
        result = num1/num2
    elif operator == "add":
        result = num1+num2
    elif operator == "subtract":
        result = num1-num2
    return result

# 5.	Calculate Rectangle Area

def calculate_area(width, height):
    return width*height

width1 = int(input())
height1 = int(input())

print(calculate_area(width1, height1))

# 4. Orders
bought_product = input()
bought_quantity = int(input())

def calculate_total_price(product, quantity):
    total_price = 0
    if product == "coffee":
        total_price = quantity*1.5
    elif product == "water":
        total_price = quantity*1
    elif product == "coke":
        total_price = quantity*1.4
    else:
        total_price = quantity*2
    return total_price


print(f"{calculate_total_price(bought_product, bought_quantity):.2f}")

'''

# 3. Repeat string


def repeat(string, number):
    new_string = string*number
    return new_string

input_string = input()
count = int(input())

print(repeat(input_string, count))





