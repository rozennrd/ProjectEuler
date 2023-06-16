"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value. - 1
    Two Pairs: Two different pairs. - 2
    Three of a Kind: Three cards of the same value. - 3
    Straight: All cards are consecutive values. - 4
    Flush: All cards of the same suit. - 5
    Full House: Three of a kind and a pair. - 6
    Four of a Kind: Four cards of the same value. - 7
    Straight Flush: All cards are consecutive values of same suit. - 8
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. - 9

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD   2C 3S 8S 8D TD    Player 2
        Pair of Fives    Pair of Eights
.....

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

// Note : T = Ten ; J = Jack (valet); Q = Queen ; K = king.

"""
from Timer import Timer

t = Timer()
t.start()

############################################################
# Test des suites
def royal_flush(liste):
    suit = liste[0][1]
    cards = ["T", "J", "Q", "K", "A"]
    for i in range(len(liste)) :
        if liste[i][0] not in cards or liste[i][1] != suit:
            return False
    return True


def straight_flush(liste):  # All cards are consecutive values of same suit.
    if straight(liste) and flush(liste):
        return True
    return False


def flush(liste):
    suit = liste[0][1]
    for card in liste:
        if card[1] != suit:
            return False
    return True


def count_cards_of_same_kind(liste):
    count = {}
    for card in liste:
        if card[0] not in count:
            count[card[0]] = 1
        else:
            count[card[0]] += 1
    return count


def four_of_a_kind(liste):
    count = count_cards_of_same_kind(liste)
    for card in count :
        if count[card]==4:
            return True
    return False


def three_of_a_kind(liste):
    count = count_cards_of_same_kind(liste)
    for card in count:
        if count[card] == 3:
            return True
    return False


def full_house(liste):  # three of a kind and a pair
    count = count_cards_of_same_kind(liste)
    if 3 in count.values() and 2 in count.values():
        return True
    return False


def two_pairs(liste):
    count = count_cards_of_same_kind(liste)
    cnt_2 = 0
    for value in count.values():
        if value == 2:
            cnt_2 += 1
    if cnt_2 == 2:
        return True
    return False


def one_pair(liste):
    count = count_cards_of_same_kind(liste)
    cnt_2 = 0
    for value in count.values():
        if value == 2:
            cnt_2 += 1
    if cnt_2 == 1:
        return True
    return False


def high_card(liste, kind_of_hand):  # Highest value card.
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    cases_highest_card_counts = [0, 5, 4, 8]
    cases_highest_paired_card_count = [1,2,3,6,7]
    if kind_of_hand in cases_highest_card_counts:
        max_index = 0
        for card in liste:
            if cards.index(card[0]) > max_index:
                max_index = cards.index(card[0])
        return max_index
    else:
        cnt = count_cards_of_same_kind(liste)
        total_points = 0
        for value in cnt:
            if cnt[value]>1:
                total_points += cnt[value] * cards.index(value)
        return total_points


def straight(liste) :  # All cards are consecutive values.
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    indexes = []
    for card in liste :
        indexes.append(cards.index(card[0]))
    indexes.sort()
    for i in range(len(indexes)-1):
        if indexes[i+1] - indexes[i] != 1:
            return False
    return True


############################################################
# Test de la main :quelle est la combinaison la plus haute contenue dans la main ?
def highest_combination(liste):
    if royal_flush(liste):
        return 9
    elif straight_flush(liste):
        return 8
    elif four_of_a_kind(liste):
        return 7
    elif full_house(liste):
        return 6
    elif flush(liste):
        return 5
    elif straight(liste):
        return 4
    elif three_of_a_kind(liste):
        return 3
    elif two_pairs(liste):
        return 2
    elif one_pair(liste):
        return 1
    return 0


def compare_two_hands(l1, l2):
    highest_l1 = highest_combination(l1)
    highest_l2 = highest_combination(l2)
    if highest_l1>highest_l2:
        return True # we want to know how many times player 1 wins, so we just count how many times this is True
    if highest_l2 == highest_l1:
        if high_card(l1, highest_l1) > high_card(l2, highest_l2): #TODO : à changer ; pour l'instant 5H 5C 6S 7S KD   2C 3S 8S 8D TD  Player 2 retourne player1 gagnant (highest value card et pas highest pair)
            return True


    return False



############################################################
# Conversion du fichier
with open("poker.txt", 'r') as file:
    fileconverted = file.readlines()
    hands = []
    for string in fileconverted:
        hands.append(string.strip('\n').split())

player1 = []
player2 = []

for liste in hands :
    player1.append(liste[:5])
    player2.append(liste[5:])

# La conversion a fonctionné, le fichier est prêt à être lu liste par liste.


cnt_p1_wins = 0
for round in range(len(player1)):
    if compare_two_hands(player1[round], player2[round]):
        cnt_p1_wins += 1

print(cnt_p1_wins)
t.stop()
print(t.elapsed)

############################################################
# TESTS

# def test(function, passes, not_passes):
#     print(f"{function.__name__}")
#     if function(passes):
#         print("....OK")
#     else:
#         print(f"....not OK : {function}({passes}) should return True, returns False")
#     if function(not_passes):
#         print(f"....not OK : {function}({not_passes}) should return False, returns True")
#     else:
#         print("....OK")



# print("TESTS")
# test(royal_flush, ["KD", "TD", "QD", "AD", "JD"], ["2D", "3C", "QH", "AC", "JD"])
# test(flush, ["AD", "TD", "QD", "2D", "JD"], ["2D", "3C", "QH", "AC", "JD"])
# test(three_of_a_kind, ["KD", "KH", "JH", "KS", "QD"], ["2D", "3C", "QH", "AC", "JD"])
# test(four_of_a_kind, ["KD", "KH", "KC", "KS", "QD"], ["2D", "3C", "QH", "AC", "JD"])
# test(full_house, ["KD", "QH", "KC", "KS", "QD"], ["2D", "3C", "QH", "AC", "JD"])
# test(two_pairs, ["KD", "KH", "QC", "AS", "QD"], ["2D", "3C", "QH", "AC", "JD"])
# # we do not test highest value
# test(straight, ["2D", "3H", "4C", "6S", "5D"], ["2D", "3C", "QH", "AC", "JD"])
# test(one_pair, ["KD", "KH", "JC", "AS", "QD"], ["2D", "3C", "QH", "AC", "JD"])
# test(straight_flush, ["2D", "3D", "4D", "6D", "5D"], ["2D", "3C", "QH", "AC", "JD"])


# def test_compare_two_hands():
#     if compare_two_hands(['8C', 'TS', 'KC', '9H', '4S'],['7D', '2S', '5D', '3S', 'AC']):
#         print(".... OK")