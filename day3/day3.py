def isSymbol(matrix, n, m, row, column) -> bool:
    return row >= 0 and row < n and column >= 0 and column < m and matrix[row][column] != '.'

def isPartNumber(matrix, n, m, row, start, end) -> bool:
    adjacentSlots = [(row - 1, start - 1), (row, start - 1), (row + 1, start - 1), (row - 1, end + 1), (row, end + 1), (row + 1, end + 1)]
    for index in range(start, end + 1):
        adjacentSlots.append((row - 1, index))
        adjacentSlots.append((row + 1, index))

    return any(list(map(lambda slot : isSymbol(matrix, n, m, slot[0], slot[1]), adjacentSlots)))

def addIfPartNumber(matrix, n, m, row, curr_start, curr_end) -> int:
    if curr_start != -1 and isPartNumber(matrix, n, m, row, curr_start, curr_end):
        return int(matrix[row][curr_start:curr_end + 1])

    return 0

def findAdjacentToPartNumber(partNumbers, neighborIndex):
    for partNumber in partNumbers:
        (row, (col_start, col_end)) = partNumber
        if neighborIndex[0] == row and neighborIndex[1] >= col_start and neighborIndex[1] <= col_end:
            return partNumber

    return (0, 0)

with open("./input.txt", "r") as input_file:
    matrix = input_file.read().splitlines()

    n, m = len(matrix), len(matrix[0])

    partNumberIndices = []
    gearIndices = []
    for row in range(n):
        curr_start, curr_end = -1, -1
        for column in range(m):
            if matrix[row][column].isdigit():
                if curr_start == -1:
                    curr_start = column
                curr_end = column
            else:
                if matrix[row][column] == "*":
                    gearIndices.append((row, column))

                if curr_start != -1 and isPartNumber(matrix, n, m, row, curr_start, curr_end):
                    partNumberIndices.append((row, (curr_start, curr_end)))
                curr_start, curr_end = -1, -1

        if curr_start != -1 and isPartNumber(matrix, n, m, row, curr_start, curr_end):
            partNumberIndices.append((row, (curr_start, curr_end)))

    sum = 0
    for index in partNumberIndices:
        sum += int(matrix[index[0]][index[1][0]:index[1][1] + 1])
    print("Part 1: {0}".format(sum))

    gearRatio = 0
    for index in gearIndices:
        (row, column) = index

        neighbourPartNumbers = set()

        neighbours = [(row - 1, column), (row + 1, column), (row - 1, column - 1), (row, column - 1), (row + 1, column - 1), (row - 1, column + 1), (row, column + 1), (row + 1, column + 1)]
        for neighbour in neighbours:
            if (adjacentPartNumber := findAdjacentToPartNumber(partNumberIndices, neighbour)) != (0, 0):
                neighbourPartNumbers.add(adjacentPartNumber)
        
        if len(neighbourPartNumbers) == 2:
            curr_gear_ratio = 1
            for partNumber in neighbourPartNumbers:
                curr_gear_ratio *= int(matrix[partNumber[0]][partNumber[1][0]:partNumber[1][1] + 1])
            gearRatio += curr_gear_ratio
    print("Part 2: {0}".format(gearRatio))