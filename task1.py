left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))


left_list.sort()
right_list.sort()

sum = 0


length = len(left_list)
if length == len(right_list):
    for number in range(length):
        sum += abs(left_list[number] - right_list[number])
        print (f'{left_list[number]} - {right_list[number]} = {abs(left_list[number] - right_list[number])}')
    
print (sum)
