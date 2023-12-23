def getCardWinningsPart2(card: str) -> int:
    winning_nums = set(map(lambda num : int(num), filter(lambda num : num.isdigit(), card.split(":")[1].split("|")[0].split(" "))))
    your_nums = list(map(lambda num : int(num), filter(lambda num : num.isdigit(), card.split(":")[1].split("|")[1].split(" "))))

    curr_winnings = 0
    for your_num in your_nums:
        if your_num in winning_nums:
            curr_winnings += 1
    
    return curr_winnings

def getCardWinnings(card: str) -> int:
    winning_nums = set(map(lambda num : int(num), filter(lambda num : num.isdigit(), card.split(":")[1].split("|")[0].split(" "))))
    your_nums = list(map(lambda num : int(num), filter(lambda num : num.isdigit(), card.split(":")[1].split("|")[1].split(" "))))

    curr_winnings = 0
    for your_num in your_nums:
        if your_num in winning_nums:
            if curr_winnings == 0:
                curr_winnings = 1
            else:
                curr_winnings *= 2

    return curr_winnings

with open("./input.txt", "r") as input_file:
    cards = input_file.read().splitlines()

    winnings = 0
    for card in cards:
        winnings += getCardWinnings(card)
    print("Part 1: {0}".format(winnings))

    cardCounts = [1] * len(cards)
    for index, card in enumerate(cards):
        curr_winnings = getCardWinningsPart2(card)
        for offset in range(curr_winnings):
            if (nextIndex := index + offset + 1) < len(cardCounts):
                cardCounts[nextIndex] += cardCounts[index]
    sum_cards = sum(cardCounts)
    print("Part 2: {0}".format(sum_cards))
    