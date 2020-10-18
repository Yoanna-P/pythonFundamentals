'''
# 1. Invert values

word = input()
first_list = word.split(" ")
second_list = []

for i in range(len(first_list)):
    first_list[i] = int(first_list[i])
    second_list.append(first_list[i]*-1)

print(second_list)

# 2.Multiples list

factor = int(input())
length = int(input())

new_list = []
i = 1

while len(new_list) < length:
    if i % factor == 0:
        new_list.append(i)
    i += 1
print(new_list)


# 3. Football cards

cards = input()
a_players_count = 11
b_players_count = 11

list_cards = cards.split(" ")
unique_list = list(set(list_cards))

for el in unique_list:
    if "A" in el:
        a_players_count -= 1
    if "B" in el:
        b_players_count -= 1

print(f"Team A - {a_players_count}; Team B - {b_players_count}")

if a_players_count < 7 or b_players_count < 7:
    print("Game was terminated")


# 4.Number beggars

numbers = input()
beggars = int(input())

list_string = numbers.split(", ")

for i in range(len(list_string)):
    list_string[i] = int(list_string[i])

for j in range(0, len(list_string), beggars):
    sum += list_string[j]

print(sum)

# 6. Survival of the Biggest

num_list = input().split(" ")
num_count = int(input())

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

for j in range(num_count):
    a = min(num_list)
    num_list.remove(a)

print(num_list)

#7. Easter Gifts

gifts = input().split(" ")

while input() != "No Money":
    input()


# 8. Seize the fire

fires = input().split("#")
water = int(input())
effort = 0
total_fire = []

RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

# Reading and splitting the data

for el in fires:
    type_of_fire, value = el.split(" = ")
    value = int(value)

    is_valid = (
            (type_of_fire == "High" and value in RANGE_HIGH) or
            (type_of_fire == "Medium" and value in RANGE_MEDIUM) or
            (type_of_fire == "Low" and value in RANGE_LOW)
    )

    if is_valid and water >= value:
        water -= value
        effort += value * 0.25
        total_fire.append(value)

print("Cells:")
for fire in total_fire:
    print(f"- {fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(total_fire)}")

# 5. Faro - my solution

cards = input().split()
n_shuffles = int(input())
small_list = cards_list[1:-1]
left_length = int(len(small_list)/2)
left_list = small_list[0:left_length]
right_list = small_list[left_length:]
shuffled_list = []

for i in range(left_length+1):
    shuffled_list.append(right_list[0])
    shuffled_list.append(left_list[0])

print(shuffled_list)


# 9. France

items = input().split("|")
budget = float(input())

prices = []
bought_prices = []
sold_prices = []
profit = 0

for el in items:
    item, price = el.split("->")
    price = float(price)

    is_valid = (
        (item == "Clothes" and price <= 50) or
        (item == "Shoes" and price <= 35) or
        (item == "Accessories" and price <= 20.50)
        )

    if is_valid and budget >= price:
        budget -= price
        profit += price*0.4
        sold_prices.append(price*1.4)

for el in sold_prices:
    print(f"{el:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if (budget + sum(sold_prices))>=150:
    print("Hello, France!")
else:
    print("Time to go.")


#5. Faro shuffle - Ines

cards = input().split()
n_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]
half = len(cards)//2

for shuffle in range(n_shuffles):

    left_cards = cards[1:half]
    right_cards = cards[half:(-1)]
    shuffled_list = []

    for i in range(len(left_cards)):
        shuffled_list.append(right_cards[i])
        shuffled_list.append(left_cards[i])

    cards = shuffled_list.copy()
    cards.insert(0, top_card)
    cards.append(bottom_card)
    shuffled_list = []

print(cards)

#5.Faro shuffle - kolega

cards = input().split()
n_shuffle = int(input())
middle = len(cards)//2

for i in range(n_shuffle):
    left_list=cards[:middle]
    right_list=cards[middle:]

    shuffled_cards = []

    for j in range(middle):
        shuffled_cards.append(left_list[j])
        shuffled_cards.append(right_list[j])
        cards = shuffled_cards

print(shuffled_cards)

#7.

gifts = input().split()
command = input()

while not command == "No Money":
    current_gift = command.split()
    if current_gift[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == current_gift[1]:
                gifts[index] = "None"
    elif current_gift[0] == "Required":
        if int(current_gift[2]) < len(gifts):
            gifts[int(current_gift[2])] = current_gift[1]
    elif current_gift[0] == "JustInCase":
        gifts[-1] = current_gift[1]
    command = input()

for el in gifts:
    if not el == "None":
        print(el, end=" ")

'''

#10 Bread - I'm only getting half the points

events = input().split("|")
old_energy = 100
new_energy = 0
coins = 100
skipped = 0

for element in events:
    event, number = element.split("-")
    number = int(number)
    if event == "rest":
        if old_energy + number > 100:
            print(f"You gained {100 - old_energy} energy.")
            old_energy = 100
        else:
            old_energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {old_energy}.")
        #new_energy = number + old_energy
        #if new_energy > 100:
         #   new_energy = 100
       # print(f"You gained {new_energy-old_energy} energy.")
        #old_energy = new_energy
        #print(f"Current energy: {old_energy}.")
    elif event == "order":
        if old_energy >= 30:
            print(f"You earned {number} coins.")
            coins += int(number)
            old_energy -= 30
        else:
            print("You had to rest!")
            old_energy += 50
            skipped += 1
    else:
        coins -= int(number)
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            skipped += 1
            break

if skipped == 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {old_energy}")



















