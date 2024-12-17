pairs = []
lists = []

try:
    with open("input5.txt", "r") as file:
        for line in file:
            try:
                numbers = [int(num) for num in line.replace("|", ",").split(",")]
                
                if len(numbers) == 2:
                    pairs.append(numbers)
                elif len(numbers) > 2:
                    lists.append(numbers)
            except ValueError:
                print(f"Невозможно преобразовать строку в числа: {line.strip()}")
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")

# Вывод результатов
print("Pairs (2 числа):", pairs)
print("Lists (больше 2 чисел):", lists)


sum = 0
for list in lists:
    check = True
    for i in range(len(list)-1):
        if check == False:
            break
        number1 = list[i]
        number2 = list[i+1]
        for pair in pairs:
            if number1 in pair and number2 in pair:
                index = pair.index(number1)
                if index != 0:
                    check = False
                break
    if check:
        middle = int(len(list)/2) 
        print (list[middle])
        sum += list[middle]

print (sum)