#!/usr/bin/env python3

import functools

lines = []
with open('day07.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

card_nums = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}


def card_to_num(card, overrides={}):
    if card in overrides:
        return overrides[card]
    if card in card_nums:
        return card_nums[card]
    return int(card)


def compare_card_counts(one, two):
    if one[1] > two[1]:
        return 1
    elif one[1] < two[1]:
        return -1
    elif one[0] > two[0]:
        return 1
    elif one[0] < two[0]:
        return -1
    return 0


def make_card_counts(cards_str):
    count_map = {}
    cards = [card_to_num(c) for c in cards_str]
    cards.sort()
    for card in cards:
        if card not in count_map:
            count_map[card] = 1
        else:
            count_map[card] += 1
    card_counts = [(k, v) for (k, v) in count_map.items()]
    card_counts.sort(key=functools.cmp_to_key(compare_card_counts), reverse=True)
    return card_counts


def rank_counts(card_counts):
    # five of a kind
    if card_counts[0][1] == 5:
        return 7

    # four of a kind
    elif card_counts[0][1] == 4:
        return 6

    # full house
    elif card_counts[0][1] == 3 and card_counts[1][1] == 2:
        return 5

    # three of a kind
    elif card_counts[0][1] == 3:
        return 4

    # two pair
    elif card_counts[0][1] == 2 and card_counts[1][1] == 2:
        return 3

    # one pair
    elif card_counts[0][1] == 2:
        return 2

    return 1


class Hand(object):
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.card_counts = make_card_counts(cards)
        self.rank = rank_counts(self.card_counts)

    def rank(self):
        return self.rank


def hand_compare(one, two, overrides=None):
    if overrides is None:
        overrides = {}
    if one.rank != two.rank:
        return 1 if one.rank > two.rank else -1
    for index in range(len(one.cards)):
        num_one, num_two = card_to_num(one.cards[index], overrides=overrides), card_to_num(two.cards[index], overrides=overrides)
        if num_one != num_two:
            return 1 if num_one > num_two else -1
    return 0

hands = []

for line in lines:
    cards, bid = line.split(' ')
    hands.append(Hand(cards, bid))

hands.sort(key=functools.cmp_to_key(hand_compare))

total = 0
for index in range(len(hands)):
    hand = hands[index]
    total += (index + 1) * hand.bid
    print(hand.cards, index + 1, hand.bid, hand.card_counts)

    for count_index in range(len(hand.card_counts)):
        num, joker_count = hand.card_counts[count_index]
        if num == 11:
            del hand.card_counts[count_index]
            if len(hand.card_counts) == 0:
                hand.card_counts.append((14, joker_count))
            else:
                hand.card_counts[0] = (hand.card_counts[0][0], hand.card_counts[0][1] + joker_count)
            print(f'Converted {joker_count} jokers to {hand.card_counts[0][0]}: {hand.card_counts}')
            hand.rank = rank_counts(hand.card_counts)
            break

print(f'Part 1: {total}')


def hand_compare_2(one, two):
    return hand_compare(one, two, overrides={'J': 1})


hands.sort(key=functools.cmp_to_key(hand_compare_2))

total = 0

for index in range(len(hands)):
    hand = hands[index]
    total += (index + 1) * hand.bid

print(f'Part 2: {total}')
