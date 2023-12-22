PREF_RED_CUBE = 12
PREF_GREEN_CUBE = 13
PREF_BLUE_CUBE = 14

def isItPossible(sets: list[int]) -> bool:
    max_red, max_green, max_blue = 0, 0, 0
    for set in sets:
        balls = set.split(",")
        for ball in balls:
            match ball.split():
                case [number, "red"]:
                    max_red = max(max_red, int(number))
                case [number, "green"]:
                    max_green = max(max_green, int(number))
                case [number, "blue"]:
                    max_blue = max(max_blue, int(number))
    
    return max_red <= PREF_RED_CUBE and max_green <= PREF_GREEN_CUBE and max_blue <= PREF_BLUE_CUBE

def getPower(sets: list[int]) -> int:
    max_red, max_green, max_blue = 0, 0, 0
    for set in sets:
        balls = set.split(",")
        for ball in balls:
            match ball.split():
                case [number, "red"]:
                    max_red = max(max_red, int(number))
                case [number, "green"]:
                    max_green = max(max_green, int(number))
                case [number, "blue"]:
                    max_blue = max(max_blue, int(number))
    
    return max_red * max_green * max_blue

with open("./input.txt", "r") as input_file:
    input = input_file.read().splitlines()

    sum_1 = 0
    sum_2 = 0
    for game in input:
        id = (game.split(":")[0]).split(" ")[1]
        sets = (game.split(":")[1]).split(";")

        if isItPossible(sets):
            sum_1 += int(id)
        
        sum_2 += getPower(sets)
    
    print("Part 1: {0}".format(sum_1))
    print("Part 2: {0}".format(sum_2))
