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

new_obstacles = set()
checked_obstacle = set()

right = False
left = False
up = False
down = False
i = -1
j = -1
start_i = -1
start_j = -1
start_dir = ""

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
            new_obstacles.add((i, j))
        i -= 1
    if i > 0 and data[i-1][j] == "#":
        change_direction("r")
        

def go_right():
    global i, j, count
    while j != num_col-1 and data[i][j+1] != "#":
        if data[i][j] == ".":
            new_obstacles.add((i, j))
        j += 1
    if j < num_rows-1 and data[i][j+1] == "#":
        change_direction("d")
    

def go_down():
    global i, j, count
    while i != num_rows-1 and data[i+1][j] != "#":
        if data[i][j] == ".":
            new_obstacles.add((i, j))
        i += 1
    if i < num_rows-1 and data[i+1][j] == "#":
        change_direction("l")   

def go_left():
    global i, j, count
    while j != 0 and data[i][j-1] != "#":
        if data[i][j] == ".":
            new_obstacles.add((i, j))
        j -= 1
    if j > 0 and data[i][j-1] == "#":
        change_direction("u") 


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

def check():
    check_stuck = False
    i = start_i
    j = start_j
    direction = start_dir

    obstacles = []
    right, down, left, up = [True,-1,-1], [True,-1,-1], [True,-1,-1], [True,-1,-1]

    while not check_stuck and right[0] == True and down[0] == True and left[0] == True and up[0] == True:
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
            for index in range(len(obstacles)-1):
                if index % 4 == (len(obstacles)-1) % 4:
                    if obstacles[len(obstacles) - 1] == obstacles[index]:
                        check_stuck = True
    
    return check_stuck


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


start_i = i
start_j = j
start_dir = check_direction()
print (right, left, down, up, i, j)
print (start_dir, start_i, start_j)


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

new_obstacles.add((i, j))

for obstacle in new_obstacles:
    data[obstacle[0]][obstacle[1]] = "#"
    if check():
        checked_obstacle.add(obstacle)
    data[obstacle[0]][obstacle[1]] = "."

print(len(checked_obstacle))



