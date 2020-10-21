# Trains
'''
wagons = int(input())
command = input()

train_length = [0 for _ in range(wagons)]

while not command == "End":
    data = command.split()
    if data[0] == "add":
        train_length[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        people = int(data[2])
        train_length[index] += int(people)
    elif data[0] == "leave":
        index = int(data[1])
        train_length[index] -= int(data[2])
    command = input()

print(train_length)

# Todo_List

command = input()
todo = []

while not command == "End":
    data = command.split("-")
    index = int(data[0])
    task = data[1]
    todo.insert(index, task)

    command = input()

print(todo)

'''

# 4. Even numbers

nums = [int(x) for x in input().split(", ")]
#even_nums_index = [i for i in range(len(nums)) if nums[i] % 2 == 0]
#print(even_nums_index)

even_nums_index = filter(lambda nums[i] : nums[i] % 2 == 0, nums)

















