import re

data = ""

with open("input3.txt", "r") as file:
    data = file.read()

pattern = r"(mul\(\d+,\d+\)|don\'t\(\)|do\(\))"

matches = re.findall(pattern, data)


sum = 0
check = True
for match in matches:   
    if "mul" in match:
        if check:
            numbers = re.findall(r"\d+", match)
            numbers = [int(num) for num in numbers]
            sum += numbers[0] * numbers[1]
    elif match == "do()":
        check = True
    elif match == "don't()":
        check = False


print(sum)

"""
sum = 0
for pair in muls:
   sum += int(pair[0]) * int(pair[1])

print(sum)
"""
