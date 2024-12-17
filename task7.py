data = []

with open("input4.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        letter_array = []
        line = line.strip()
        for letter in line:
            letter_array.append(letter)
        data.append(letter_array)


num_rows = len(data)
num_col = len (data[0])
count = 0


for i in range(num_rows):
    for j in range(num_col):
        if j < num_col-3:
            if (
                data[i][j] == "X"
                and data[i][j + 1] == "M"
                and data[i][j + 2] == "A"
                and data[i][j + 3] == "S"
            ) or (
                data[i][j] == "S"
                and data[i][j + 1] == "A"
                and data[i][j + 2] == "M"
                and data[i][j + 3] == "X"
            ):
                count += 1

        if i < num_rows-3:
            if (
                data[i][j] == "X" 
                and data[i+1][j] == "M" 
                and data[i+2][j] == "A" 
                and data[i+3][j] == "S"
            ) or (
                data[i][j] == "S" 
                and data[i+1][j] == "A" 
                and data[i+2][j] == "M" 
                and data[i+3][j]== "X"
            ):
                count += 1       

        if i < num_rows-3 and j < num_col-3:
            if (
                data[i][j] == "X" 
                and data[i+1][j+1] == "M" 
                and data[i+2][j+2] == "A" 
                and data[i+3][j+3] == "S"
            ) or (
                data[i][j] == "S" 
                and data[i+1][j+1] == "A" 
                and data[i+2][j+2] == "M" 
                and data[i+3][j+3] == "X"
            ):
                count += 1
        if j < num_col-3 and i > 2:
            if (
                data[i][j] == "X" 
                and data[i-1][j+1] == "M" 
                and data[i-2][j+2] == "A" 
                and data[i-3][j+3] == "S"
            ) or (
                data[i][j] == "S" 
                and data[i-1][j+1] == "A" 
                and data[i-2][j+2] == "M" 
                and data[i-3][j+3] == "X"
            ):
                count += 1


print(count)
