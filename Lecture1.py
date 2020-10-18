# Biggest of three numbers
"""
a = int(input())
b = int(input())
c = int(input())

print(max(a,b,c))

OR

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
"""
# Number Definer
"""
a = float(input())

if a == 0:
    print("zero")
elif a<0:
    if a > -1:
        print("small negative")
    elif a >= -1000000:
        print("negative")
    else:
        print("large negative")
elif a > 0:
    if a < 1:
        print("small positive")
    elif a > 1000000:
        print("large positive")
    else:
        print("positive")

# 2ри вариант

n = float(input())

if n == 0:
    print("zero")
else:
    if abs(n) < 1:
        print("small", end=" ")
    elif abs(n) > 1000000:
        print("large", end=" ")
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
"""
# Loops - Word reverse
"""
for x in range(3):
    if x == 1:
        continue
    print(x)

x = "Python"

print(x[5])

for i in x:
    print(len(x)-i)


word = input()
reversed_word = ""

for i in range(len(word) -1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

word = input()
reversed_word = ""

i = len(word)-1
while i > 0:
    reversed_word += word[i]
    i -=1


word = input()
new_word =""

for a in word:
    new_word += a
print(new_word)

i=0
word = input()
while i < len(word):
    print(word[i])
    i+=1

word = input()
new_word =""

for a in range(len(word)-1, -1, -1):
    new_word += word[a]
print(new_word)


x = input()
print(x[::-1])

# Loops - Number between 1 and 100

while True:
    n = float(input())
    if 1 <= n <= 100:
        print(f"The number {n} is between 1 and 100")
        break

# Number between 1 and 100 / вариант 2

number = float(input())
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number} is between 1 and 100")


# Patterns

grow = 1
shrink = -1

desired_size = int(input())
current_size = 1
direction = grow

while 0 < current_size < (desired_size+1):
    print("*"*current_size)
    current_size += direction

    if desired_size == current_size:
        direction = shrink
"""

# Patterns - variant 2

size = int(input())

for i in range(1, size +1):
    print(i*"*")
for j in range (size-1, 0, -1):
    print(j*"*")
