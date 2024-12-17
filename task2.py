left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))


sum = 0
for number in left_list:
    count = right_list.count(number)
    sum += number * count

print (sum)