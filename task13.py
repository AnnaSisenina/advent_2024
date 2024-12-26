data = []

with open("input7.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(":")
        numbers = list(map(int, parts[1].strip().split()))
        data.append((int(parts[0]), numbers))

total_sum = 0


for line in data:
    check = False
    check_sum = line[0]
    num_operations = len(line[1]) -1
    num_combinations = 2**num_operations
    for i in range (num_combinations):
        sum = line[1][0]
        binary = bin(i)[2:].zfill(num_operations)
        operations = [int(bit) for bit in binary]
        for i in range(num_operations):
            if operations[i] == 0:
                sum += line[1][i+1]
            elif operations[i] == 1:
                sum *= line[1][i+1]
        if sum == check_sum:
            check = True
            break
    if check:
        total_sum += check_sum

print(total_sum)

        

