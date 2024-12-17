data = []

with open("input6.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        symbol_array = []
        line = line.strip()
        for symbol in line:
            symbol_array.append(symbol)
        data.append(symbol_array)


num_rows = len(data)
num_col = len (data[0])
count = 1

for string in data:
    print (string)

right = False
left = False
up = False
down = False
i = -1
j = -1


def change_direction(direction):
    global right, left, up, down
    if direction == "r":
        right = True
        left = up = down = False
    if direction == "l":
        left = True
        up = down = right = False
    if direction == "u":
        up = True
        right = left = down = False
    if direction == "d":
        down = True
        right = left = up = False

def check_direction():
    global right, left, up, down
    if right: return "r"
    if left: return "l"
    if up: return "u"
    else: return "d"



def go_up():
    global i, j, count
    while  i != 0 and data[i-1][j] != "#":
        if data[i][j] == ".":
            count += 1
            data[i][j] = "X"
        i -= 1
    if i > 0 and data[i-1][j] == "#":
        change_direction("r")

def go_right():
    global i, j, count
    while j != num_col-1 and data[i][j+1] != "#":
        if data[i][j] == ".":
            count += 1
            data[i][j] = "X"
        j += 1
    if j < num_rows-1 and data[i][j+1] == "#":
        change_direction("d")

def go_down():
    global i, j, count
    while i != num_rows-1 and data[i+1][j] != "#":
        if data[i][j] == ".":
            count += 1
            data[i][j] = "X"
        i += 1
    if i < num_rows-1 and data[i+1][j] == "#":
        change_direction("l")

def go_left():
    global i, j, count
    while j != 0 and data[i][j-1] != "#":
        if data[i][j] == ".":
            count += 1
            data[i][j] = "X"
        j -= 1
    if j > 0 and data[i][j-1] == "#":
        change_direction("u")

for line in data:
    for symbol in line:
        if symbol == "^": 
            change_direction("u")
            i = data.index(line)
            j = line.index(symbol)
            break
        if symbol == ">": 
            change_direction("r")
            i = data.index(line)
            j = line.index(symbol)
            break
        if symbol == "<":
            change_direction("l")
            i = data.index(line)
            j = line.index(symbol)
            break
        if symbol == "v":
            change_direction("d")
            i = data.index(line)
            j = line.index(symbol)
            break
print (right, left, down, up, i, j)

data[i][j] = "X"
while i != 0 and j != 0 and i != num_rows-1 and j != num_col-1:
    direction = check_direction()
    if direction == "u":
        go_up()
    if direction == "r":
        go_right()
    if direction == "d":
        go_down()
    if direction == "l":
        go_left()
data[i][j] = "X"
count += 1

for string in data:
    print (string)

print (count)