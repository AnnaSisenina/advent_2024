def checkDescending(report):
    for i in range (len(report)-1):
        if (report[i]-report[i+1]) > 3 or (report[i]-report[i+1]) <= 0 :
            return False
    return True

def loopWOElement(report, i):
    copyOfReport = report.copy()
    del copyOfReport[i]
    return copyOfReport

def checkDescWithPrDemp(report):
    count = 0
    
    if checkDescending(report):
        return True
    else:
        for i in range (len(report)-1):
            if (report[i]-report[i+1]) > 3 or (report[i]-report[i+1]) <= 0:
                count += 1
                if count > 1: 
                    return False
                if i==0:
                    check = checkDescending(loopWOElement(report, i)) or checkDescending(loopWOElement(report, i+1))
                    return check
                else:
                    check = checkDescending(loopWOElement(report, i)) or checkDescending(loopWOElement(report, i-1)) or checkDescending(loopWOElement(report, i+1))
                    return check
        return check

my_list = [67, 66, 64, 61, 76, 60, 57]

print(checkDescWithPrDemp(my_list))
