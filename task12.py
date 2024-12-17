data = []

with open("input6_test.txt", "r") as file:
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

def check_right(p, q):
    check_pq = False
    while q < num_col-1:
        if data[p][q] == "#":
            check_pq = True
            break
        q += 1
    if check_pq:
            return [True, [p, q-1]]
    return [False, [-1, -1]]

def check_down(p, q):
    check_pq = False
    while p < num_rows-1:
        if data[p][q] == "#":
            check_pq = True
            break
        p += 1
    if check_pq:
            return [True, [p-1, q]]
    return [False, [-1, -1]]

def check_left(p, q):
    check_pq = False
    while q > 0:
        if data[p][q] == "#":
            check_pq = True
            break
        q -= 1
    if check_pq:
            return [True, [p, q+1]]
    return [False, [-1, -1]]

def check_up(p, q):
    check_pq = False
    while p > 0:
        if data[p][q] == "#":
            check_pq = True
            break
        p -= 1
    if check_pq:
            return [True, [p+1, q]]
    return [False, [-1, -1]]

def check_square (a, b, c, d):
    if (a[0] - b[0] == d[0] - c[0] 
                    ) and (
                        a[1] - b[1] == d[1] - c[1] 
                    ) and (
                        a[0] - d[0] == b[0] - c[0] 
                    ) and (
                        a[1] - d[1] == b[1] - c[1] 
                    ):
        return True
    return False
        

def go_up():
    global i, j, count
    while  i != 0 and data[i][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "|"
            right = check_right(i,j)
            down = check_down(*right[1])
            left = check_left(*down[1])
            if right[0] and down[0] and left[0]:
                if check_square([i, j], right[1], down[1], left[1]):
                    count += 1
        i -= 1
    i+=1
    if i > 0 and data[i-1][j] == "#":
        change_direction("r")



def go_right():
    global i, j, count
    while j != num_col-1 and data[i][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "-"
            down = check_down(i,j)
            left = check_left(*down[1])
            up = check_up(*left[1])
            if up[0] and down[0] and left[0]:
                if check_square(up[1], [i, j], down[1], left[1]):
                    count += 1
        j += 1
    j-=1
    if j < num_rows-1 and data[i][j+1] == "#":
        change_direction("d")

       

def go_down():
    global i, j, count
    while i != num_rows-1 and data[i][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "|"
            left = check_left(i,j)
            up = check_up(*left[1])
            right = check_right(*up[1])
            if left[0] and up[0] and right[0]:
                if check_square(right[1], [i, j], left[1], up[1]):
                    count += 1
        i += 1
    i-=1
    if i < num_rows-1 and data[i+1][j] == "#":
        change_direction("l")

def go_left():
    global i, j, count
    while j != 0 and data[i][j] != "#":
        if data[i][j] == ".":
            data[i][j] = "-"
            up = check_up(i,j)
            right = check_right(*up[1])
            down = check_down(*right[1])
            if up[0] and right[0] and down[0]:
                if check_square(right[1], down[1], [i, j], up[1]):
                    count += 1
        j -= 1
    j+=1
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



for string in data:
    print (string)

print (count)