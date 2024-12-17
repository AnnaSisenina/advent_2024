data = []

with open('input2.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        data.append(numbers)


count=0

def delta(report):
    delta = []
    for i in range(len(report)-1):
        delta.append((report[i]-report[i+1]))
    return sum(delta)

def checkDescending(report):
    for i in range (len(report)-1):
        if (report[i]-report[i+1]) > 3 or (report[i]-report[i+1]) <= 0 :
            return False  
    return True
        
def checkAscending(report):
    for i in range (len(report)-1):
        if (report[i]-report[i+1]) >= 0 or (report[i]-report[i+1]) < -3 :
            return False
    return True

for report in data:
    check = True
    reportDelta = delta(report)

    if reportDelta == 0:
         check = False
    if reportDelta > 0:
         check = checkDescending(report)
    if reportDelta < 0:
        check = checkAscending(report)
            
    if check:
         count+=1
 
print(count)    

