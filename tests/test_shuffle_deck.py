from main import deck_of_cards, shuffle_deck

def test_shuffle_deck_decks_are_same_length_after_shuffle():
    # Act
    shuffled_deck = shuffle_deck(deck_of_cards)
    # Assert
    assert len(shuffled_deck) == len(deck_of_cards)

def test_shuffle_deck_order_is_shuffled():
    # Act
    shuffled_deck = shuffle_deck(deck_of_cards)
    # Assert
    assert shuffled_deck != deck_of_cards

def test_shuffle_deck_shuffles_smaller_hand():
    # Arrange
    smaller_hand = ["2♥", "8♦", "K♠", "2♣"]
    # Act
    shuffled_deck = shuffle_deck(smaller_hand)
    # Assert
    assert shuffled_deck != smaller_hand

def test_shuffle_deck_smaller_hands_same_length_after_shuffle():
    # Arrange
    smaller_hand = ["2♥", "8♦", "K♠", "2♣"]
    # Act
    shuffled_deck = shuffle_deck(smaller_hand)
    # Assert
    assert len(shuffled_deck) == len(smaller_hand)
