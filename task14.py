data = []

with open("input7.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(":")
        numbers = list(map(int, parts[1].strip().split()))
        data.append((int(parts[0]), numbers))

total_sum = 0


def check(line):
    check_sum = line[0]
    num_operations = len(line[1]) -1
    num_combinations = 2**num_operations
    for i in range (num_combinations):
        sum = line[1][0]
        binary = bin(i)[2:].zfill(num_operations)
        operations = [int(bit) for bit in binary]
        for j in range(num_operations):
            if operations[j] == 0:
                sum += line[1][j+1]
            elif operations[j] == 1:
                sum *= line[1][j+1]
        if sum == check_sum:
            return True
    return False

def ternary(num):
    ternary_array = []
    while num > 0:
        ternary_array.append(num % 3)
        num = int(num / 3)
    ternary_array.reverse()
    ternary = "".join(str(num) for num in ternary_array)
    return ternary

def check_conc(line):
    check_sum = line[0]
    num_operations = len(line[1])-1
    num_combinations = 3**num_operations
    ternary_num_op = ""
    for i in range (num_combinations):
        sum = line[1][0]
        ternary_num_op = ternary(i).zfill(num_operations)
        for j in range(num_operations):
            if ternary_num_op[j] == '0':
                sum += line[1][j+1]
            elif ternary_num_op[j] == '1':
                sum *= line[1][j+1]
            elif ternary_num_op[j] == '2':
                sum = int(str(sum) + str(line[1][j+1]))
        if sum == check_sum:
            return True
    return False

    


for line in data:
    if check(line):
        total_sum += line[0]
    elif check_conc(line):
        total_sum += line[0]


print(total_sum)

        

