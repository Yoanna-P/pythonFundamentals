'''
string = "hello"
a = list(string)

for i in a:
    print(ord(i))


list = [5, "hi", True, 4.5, 8]
new_list = []

for i in list:
    if type(i) == int:
        new_list.append(i)

print(new_list)

#Courses

n = int(input())
list = []

for i in range(n):
    a=input()
    list.append(a)

print(list)


#List Statistics

n = int(input())
list_positive = []
list_negative = []

for i in range(n):
    num = int(input())
    if num >= 0:
        list_positive.append(num)
    else:
        list_negative.append(num)

count_positives = len(list_positive)
sum_of_negatives = sum(list_negative)

print(list_positive)
print(list_negative)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")

# 4. Search

n = int(input())
word = input()
words = []
match_words = []

for i in range(n):
    current_word = input()
    words.append(current_word)
    if word in current_word:
        match_words.append(current_word)

print(words)
print(match_words)

'''

#5. Numbers Filter

n = int(input())
numbers = []
sorted_numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == "even":
    for el in numbers:
        if el % 2 == 0:
            sorted_numbers.append(el)
if command == "odd":
    for el in numbers:
        if not el % 2 == 0:
            sorted_numbers.append(el)
if command == "negative":
    for el in numbers:
        if el < 0:
            sorted_numbers.append(el)
if command == "positive":
    for el in numbers:
        if el >= 0:
            sorted_numbers.append(el)
print(sorted_numbers)















