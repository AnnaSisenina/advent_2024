import pandas as pd

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
count = 0
test = []

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

def check_right(p, q):
    check_pq = False
    while q <= num_col-1:
        if data[p][q] == "#":
            check_pq = True
            break
        q += 1
    if check_pq:
        return [check_pq, [p, q-1], [p, q]] # True/False; point to go; coordinates of obstacle
    return [check_pq, [-1, -1], [-1, -1]]

def check_down(p, q):
    check_pq = False
    while p <= num_rows-1:
        if data[p][q] == "#":
            check_pq = True
            break
        p += 1
    if check_pq:
        return [check_pq, [p-1, q], [p, q]]
    return [check_pq, [-1, -1], [-1, -1]]

def check_left(p, q):
    check_pq = False
    while q >= 0:
        if data[p][q] == "#":
            check_pq = True
            break
        q -= 1
    if check_pq:
        return [True, [p, q+1], [p, q]]
    return [False, [-1, -1], [-1, -1]]

def check_up(p, q):
    check_pq = False
    while p >= 0:
        if data[p][q] == "#":
            check_pq = True
            break
        p -= 1
    if check_pq:
        return [True, [p+1, q], [p, q]]
    return [False, [-1, -1], [-1, -1]]


def check(dir, a, b):
    global data
    check_stuck = False
    i = a
    j = b
    text = ""
    return_i = -1
    return_j = -1

    direction = dir
    obstacles = []
    right, down, left, up = [True,-1,-1], [True,-1,-1], [True,-1,-1], [True,-1,-1]
    if direction == "u":
        obstacles.append([i-1,j])
        text = data[i-1][j]
        return_i = i-1
        return_j = j
        data[i-1][j] = "#"
        direction = "r"
    elif direction == "r":
        obstacles.append([i,j+1])
        text = data[i][j+1]
        return_i = i
        return_j = j+1
        data[i][j+1] = "#"
        direction = "d"
    elif direction == "d":
        obstacles.append([i+1,j])
        text = data[i+1][j]
        return_i = i+1
        return_j = j
        data[i+1][j] = "#"
        direction = "l"
    elif direction == "l":
        obstacles.append([i,j-1])
        text = data[i][j-1]
        return_i = i
        return_j = j-1
        data[i][j-1] = "#"
        direction = "u"

    while len(obstacles) < 200 and not check_stuck and right[0] == True and down[0] == True and left[0] == True and up[0] == True:
        if direction == "u":
            up = check_up(i, j)
            if up[0]:
                obstacles.append(up[2])
                direction = "r"
                i = up[1][0]
                j = up[1][1]
        if direction == "r":    
            right = check_right(i, j)
            if right[0]:
                obstacles.append(right[2])
                direction = "d"
                i = right[1][0]
                j = right[1][1]
        if direction == "d":
            down = check_down(i, j)
            if down[0]:
                obstacles.append(down[2])
                direction = "l"
                i = down[1][0]
                j = down[1][1]    
        if direction == "l":
            left = check_left(i, j)
            if left[0]:
                obstacles.append(left[2])
                direction = "u"
                i = left[1][0]
                j = left[1][1]              
            
        if len(obstacles) > 4:
            if len(obstacles) % 4 != 0 and obstacles[0][0] == obstacles[len(obstacles)-len(obstacles)%4][0] and obstacles[0][1] == obstacles[len(obstacles)-len(obstacles)%4][1]:
                check_stuck = True
            elif len(obstacles) % 4 == 0 and obstacles[0][0] == obstacles[len(obstacles) - 4][0] and obstacles[0][1] == obstacles[len(obstacles) - 4][1]:
                check_stuck = True
                

    if check_stuck:
        test.append([obstacles[0][0],obstacles[0][1]])
    data[return_i][return_j]=text
    return check_stuck

def go_up():
    global i, j, count
    
    while  i != 0 and data[i-1][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "|"
        if check("u", i, j):
            count += 1
        i -= 1
    if i > 0 and data[i-1][j] == "#":
        change_direction("r")



def go_right():
    global i, j, count
    while j != num_col-1 and data[i][j+1] != "#":
        if data[i][j] == ".":
            data[i][j] = "-"
        if check("r", i, j):
            count += 1
        j += 1
    if j < num_rows-1 and data[i][j+1] == "#":
        change_direction("d")


def go_down():
    global i, j, count
    while i != num_rows-1 and data[i+1][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "|"
        if check("d", i, j):
            count += 1
        i += 1
    if i < num_rows-1 and data[i+1][j] == "#":
        change_direction("l")

def go_left():
    global i, j, count
    while j != 0 and data[i][j-1] != "#":
        if data[i][j] == ".":
            data[i][j] = "-"
        if check("l", i, j):
            count += 1
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




print(len(test))
unique_arrays = []
for array in test:
    if array not in unique_arrays:
        unique_arrays.append(array)

print(len(unique_arrays))
print (count)