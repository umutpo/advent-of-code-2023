DIGIT_STRINGS = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

def getCalibrationValueNoDigit(line: str, start: int, increment: int):
    didEncounterCalibrationValue = False
    while not didEncounterCalibrationValue:
        if line[start].isdigit():
            didEncounterCalibrationValue = True
        else:
            for DIGIT_TEXT in DIGIT_STRINGS.keys():
                if line.find(DIGIT_TEXT, start) == start:
                    line = line[:start] + str(DIGIT_STRINGS[DIGIT_TEXT]) + line[start + len(DIGIT_TEXT):]
                    didEncounterCalibrationValue = True
                    break

        start += increment

    return line

def getCalibrationValuePartTwo(line: str) -> int:
    line = getCalibrationValueNoDigit(line, 0, 1)
    line = getCalibrationValueNoDigit(line, len(line) - 1, -1)

    return getCalibrationValue(line)

def getCalibrationValue(line: str) -> int:
    left = 0
    while left < len(line) and not line[left].isdigit():
        left += 1

    right = len(line) - 1
    while right >= 0 and not line[right].isdigit():
        right -= 1
    
    if left < len(line) and right >= 0:
        return int(line[left]) * 10 + int(line[right])

    return 0
            

with open("./input.txt", "r") as input_file:
    input = input_file.read().splitlines()

    sum_1, sum_2 = 0, 0
    for line in input:
        sum_1 += getCalibrationValue(line)
        sum_2 += getCalibrationValuePartTwo(line)
    
    print("Part 1: The sum of all calibration values is {0}".format(sum_1))
    print("Part 2: The sum of all calibration values is {0}".format(sum_2))
