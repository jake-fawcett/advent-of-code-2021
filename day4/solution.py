bingo_input = open("input.txt", "r")
bingo_input = [i[:-1] for i in bingo_input]

bingo_numbers = bingo_input[0].split(",")


def check_win(bingo_card):
    for i in range(0, 5):
        vertical_win = False if False in [True if x is True else False for x in bingo_card[i::5]] else True
        horizontal_win = False if False in [True if x is True else False for x in bingo_card[i*5:(i+1)*5]] else True
        if vertical_win or horizontal_win:
            return True


def get_score(bingo_card, current_number):
    score = 0
    for i in bingo_card:
        if i != True:
            score += int(i)
    return score * int(current_number)


bingo_cards = []
i = 0
for input in bingo_input[1:]:
    if input == "":
        if i != 0:
            bingo_cards.append(bingo_card)
        bingo_card = []
        i += 1
        continue
    bingo_card += input.replace("  ", " ").split(" ")

for number in bingo_numbers:
    winning_cards = []
    for n, bingo_card in enumerate(bingo_cards):
        if number in bingo_card:
            bingo_card = [True if x == number else x for x in bingo_card]
            bingo_cards[n] = bingo_card
            if check_win(bingo_card):
                winning_cards.append(bingo_card)
                print(get_score(bingo_card, number))

    for winning_card in winning_cards:
        bingo_cards = [card for card in bingo_cards if card != winning_card]
