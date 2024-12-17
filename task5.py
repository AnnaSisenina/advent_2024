import re

data = ""

with open("input3.txt", "r") as file:
   data = file.read()

pattern = r'mul\((\d+),(\d+)\)'

muls = re.findall(pattern, data)


sum = 0

for pair in muls:
   sum += int(pair[0]) * int(pair[1])

print(sum)