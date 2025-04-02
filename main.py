from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    """
    input: deck_of_cards (list)
    output: shuffled_deck (list)

    Takes a list (deck_of_cards) argument and creates a new list
    (shuffled_deck) with the elements of the old list shuffled randomly.
    Returns the new shuffled_deck list.
    """
    deck_size = len(deck_of_cards)
    shuffled_deck = []
    already_shuffled = []

    for i in range(deck_size):
        random_card = randint(0, deck_size - 1)

        if random_card not in already_shuffled:
            shuffled_deck.append(deck_of_cards[random_card])

    return shuffled_deck
