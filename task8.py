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
        if i < num_rows-2 and j < num_col-2:
            if ((
                data[i][j] == "M" 
                and data[i+1][j+1] == "A" 
                and data[i+2][j+2] == "S"
            ) or (
                data[i][j] == "S" 
                and data[i+1][j+1] == "A" 
                and data[i+2][j+2] == "M" 
            )) and ((
                data[i][j+2] == "M" 
                and data[i+2][j] == "S"
            ) or (
                data[i][j+2] == "S" 
                and data[i+2][j] == "M" 
            )):
                count += 1
                
  
print(count)