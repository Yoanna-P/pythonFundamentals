# Jenny's message
'''
name = input()

if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")

# Drink something

age = int(input())

if age <=14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
else:
    print("drink whisky")

# Leo Oscars

num = int(input())

if num == 88:
    print("Leo finally won the Oscar! Leo is happy")
elif num == 86:
    print("Not even for Wolf of Wall Street?!")
else:
    if num > 88:
        print("Leo got one already!")
    else:
        print("When will you give Leo an Oscar?")


# Double Char

string = input()

for i in range(0, len(string)):
    print(string[i]*2, end="")

# Count sheep

num = int(input())
i=1
while i <= num:
    print(f"{i} sheep...", end="")
    i+=1


# Next happy year

year = int(input())

while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        print(year)
        break

# maximum multiple

divisor = int(input())
bound = int(input())

for i in range(bound, 0, -1):
    if i % divisor == 0:
        print(i)
        break

# mutate strings

# 8. mutate strings

string1 = input()
string2 = input()
length = len(string1)

cur_string = ""
previous_string = string1

for iteration in range(0, length):
    for index2 in range(0, iteration+1):
        cur_string += string2[index2]
    for index1 in range(iteration+1, length):
        cur_string += string1[index1]
    if not cur_string == previous_string:
        print(cur_string)
    previous_string = cur_string
    cur_string = ""


# easter cozonac

budget = float(input())
flour = float(input())

pack_eggs = 0.75*flour
milk = 1.25*flour

price_cozunak = pack_eggs + flour + milk/4

cozunak_count = int(budget/price_cozunak)
money_left = round((budget - cozunak_count*price_cozunak),2)
eggs = 0

for i in range(1, cozunak_count+1)
    if cozunak_count%3 = 0
        eggs -=
    eggs += 3

print(eggs)


# christmas spirit

quantity = int(input())
days = int(input())

ornament = 2
skirt = 5
garland = 3
light = 15

cost = 0
spirit = 0

for day in range(1, days+1):
    if day%11==0:
        quantity+=2
    if day%2 == 0:
        cost += ornament*quantity
        spirit += 5
    if day%3 == 0:
        cost += skirt * quantity + garland*quantity
        spirit += 13
    if day % 5 == 0:
        cost += light * quantity
        spirit += 17
        if day%3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += skirt + garland + light

if days%10 == 0:
    spirit -=30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")

num = int(input())

leng = len(str(num))
unique = len(set(str(num)))

while True:
    num += 1
    if leng == unique:
        print(num)
        break

'''
budget = float(input())
price_flour = float(input())

price_eggs = 0.75*price_flour
price_milk = 1.25*price_flour
price_cozunak = price_eggs + price_flour + price_milk/4
countOfCozonacs = 0
coloredEggs = 0
total_sum = 0

while budget > price_cozunak*(countOfCozonacs+1):
    countOfCozonacs += 1
    coloredEggs += 3
    total_sum = price_cozunak*countOfCozonacs
    if countOfCozonacs % 3 == 0:
        coloredEggs -= countOfCozonacs - 2

moneyLeft = budget - total_sum

print(f"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft:.2f}BGN left.")



