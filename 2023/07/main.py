def parse(filename):
    with open(filename) as f:
        data = [l.split() for l in f.read().splitlines()]

    return data


def get_hand_type(hand: str, joker=False):
    hand_dict = {}
    for c in hand:
        hand_dict[c] = hand_dict.get(c, 0) + 1

    if joker:
        if "J" in hand_dict:
            joker_count = hand_dict["J"]
            if joker_count < 5:
                del hand_dict["J"]
                card_max_count = max(hand_dict, key=hand_dict.get)
                hand_dict[card_max_count] += joker_count

    vals = hand_dict.values()

    if 5 in vals:
        return 7  # "five-of-a-kind"
    elif 4 in vals:
        return 6  # "four-of-a-kind"
    elif 3 in vals and 2 in vals:
        return 5  # "full-house"
    elif 3 in vals:
        return 4  # "three-of-a-kind"
    elif list(vals).count(2) == 2:
        return 3  # "two-pairs"
    elif 2 in vals:
        return 2  # "one-pair"

    return 1  # "high-card"


def get_card_rank(card, joker=False):
    card_rank = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    if joker:
        card_rank["J"] = 1

    if card in card_rank:
        return card_rank[card]
    return int(card)


def get_hand_strength(hand, joker=False):
    hand_strength = []
    hand_strength.append(get_hand_type(hand, joker=joker))
    for c in hand:
        hand_strength.append(get_card_rank(c, joker=joker))
    return hand_strength


def solve(hands, joker=False):
    ranks = []
    for hand, bid in hands:
        ranks.append((get_hand_strength(hand, joker=joker), hand, int(bid)))

    ranks.sort()

    total_winnings = 0
    for i, (_, hand, bid) in enumerate(ranks):
        total_winnings += bid * (i + 1)

    return total_winnings


if __name__ == "__main__":
    hands = parse("input.txt")
    print("P1:", solve(hands, joker=False))
    print("P2:", solve(hands, joker=True))
