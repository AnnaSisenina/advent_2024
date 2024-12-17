data = []

with open("input2.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        data.append(numbers)

count = 0


def delta(report):
    delta = []
    for i in range(len(report) - 1):
        delta.append((report[i] - report[i + 1]))
    return sum(delta)


def checkDescending(report):
    for i in range(len(report) - 1):
        if (report[i] - report[i + 1]) > 3 or (report[i] - report[i + 1]) <= 0:
            return False
    return True


def checkAscending(report):
    for i in range(len(report) - 1):
        if (report[i] - report[i + 1]) >= 0 or (report[i] - report[i + 1]) < -3:
            return False
    return True

def loopWOElement(report, i):
    copyOfReport = report.copy()
    del copyOfReport[i]
    return copyOfReport


def checkDescWithPrDemp(report):
    check = False
    if checkDescending(report):
        return True
    else:
        for i in range(len(report) - 1):
            if (report[i] - report[i + 1]) > 3 or (report[i] - report[i + 1]) <= 0:
                if i == 0:
                    check = checkDescending(loopWOElement(report, i)) or checkDescending(
                        loopWOElement(report, i + 1)
                    )
                    return check
                else:
                    check = (
                        checkDescending(loopWOElement(report, i))
                        or checkDescending(loopWOElement(report, i - 1))
                        or checkDescending(loopWOElement(report, i + 1))
                    )
                    return check
        return check


def checkAscWithPrDemp(report):
    check = False
    if checkAscending(report):
        return True
    else:
        for i in range(len(report) - 1):
            if (report[i] - report[i + 1]) >= 0 or (report[i] - report[i + 1]) < -3:
                if i == 0:
                    check = checkAscending(loopWOElement(report, i)) or checkAscending(
                        loopWOElement(report, i + 1)
                    )
                    return check
                else:
                    check = (
                        checkAscending(loopWOElement(report, i))
                        or checkAscending(loopWOElement(report, i - 1))
                        or checkAscending(loopWOElement(report, i + 1))
                    )
                    return check
        return check


for report in data:
    check = True
    reportDelta = delta(report)

    if reportDelta == 0:
        check = False
    if reportDelta > 0:
        check = checkDescWithPrDemp(report)
    if reportDelta < 0:
        check = checkAscWithPrDemp(report)
    if check:
        count += 1

print(count)
