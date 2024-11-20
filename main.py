import random

def create_deck():
    """
    Creates a standard Uno deck with cards of four colors, numbers 0-9,
    special cards (Skip, Reverse, Draw Two), and wild cards (Wild, Wild Draw Four).
    Returns the shuffled deck as a list of dictionaries.
    """
    colors = ['Red', 'Blue', 'Green', 'Yellow']
    numbers = list(range(0, 10))  # Numbers 0 to 9
    special_cards = ['Skip', 'Reverse', 'Draw Two']
    wild_cards = ['Wild', 'Wild Draw Four']
    deck = []

    # Add number cards to the deck
    for color in colors:
        for number in numbers:
            card = {'color': color, 'number': number}
            deck.append(card)

    # Add special cards to the deck
    for color in colors:
        for special in special_cards:
            card = {'color': color, 'special': special}
            deck.append(card)

    # Add wild cards (no color needed)
    for wild in wild_cards:
        card = {'special': wild}
        deck.append(card)
        deck.append(card)  # Typically, two of each Wild card in a deck

    # Shuffle the deck
    random.shuffle(deck)
    return deck

def draw_cards(deck, num, discard_pile=[]):
    """
    Draws a specified number of cards from the deck. If the deck is empty,
    the discard pile (except the top card) is recycled to form a new shuffled deck.
    """
    if len(deck) < num:
        print("Not enough cards in the deck. Recycling discard pile...")
        top_card = discard_pile[-1]  # Preserve the top card
        discard_pile = discard_pile[:-1]  # Remove the top card from the pile
        random.shuffle(discard_pile)  # Shuffle the remaining discard pile
        deck = discard_pile  # Reassign the discard pile as the new deck
        discard_pile = [top_card]  # Keep the top card as the discard pile
        print(f"Deck has been replenished with {len(deck)} cards.")

    drawn_cards = deck[:num]
    deck = deck[num:]
    return drawn_cards, deck, discard_pile

def valid_move(card, top_card):
    """
    Checks if the selected card can be played on the top card of the discard pile.
    A Wild card can be played on any card.
    """
    if card.get('special') in ['Wild', 'Wild Draw Four']:
        return True  # Wild cards are always valid
    if 'special' in card and 'special' in top_card:
        return card['color'] == top_card['color'] or card['special'] == top_card['special']
    return card['color'] == top_card['color'] or card.get('number') == top_card.get('number')

def initialize_game(deck):
    """
    Initializes the Uno game by dealing cards to players and setting up the discard pile.
    """
    players = {'Player 1': [], 'Player 2': []}

    # Deal 5 cards to each player
    for player in players:
        players[player], deck, _ = draw_cards(deck, 5)

    # Set up the discard pile
    discard_pile = []
    discard_card, deck, _ = draw_cards(deck, 1)
    discard_pile.append(discard_card[0])

    return players, deck, discard_pile

def play_turn(player, players, deck, discard_pile, turn_order):
    """
    Handles the player's turn in the Uno game, including drawing cards
    and processing special card effects.
    """
    print(f"\n{player}'s Turn!")
    print(f"Top card on the discard pile: {discard_pile[-1]}")
    print(f"{player}'s hand: {players[player]}")

    # Find valid cards to play
    valid_cards = [card for card in players[player] if valid_move(card, discard_pile[-1])]

    if valid_cards:
        print("You have the following valid cards to play:")
        for idx, card in enumerate(valid_cards, 1):
            print(f"{idx}: {card}")

        choice = int(input("Choose a card to play (1 to n), or enter 0 to skip: "))
        if choice > 0 and choice <= len(valid_cards):
            card_to_play = valid_cards[choice - 1]
            players[player].remove(card_to_play)
            discard_pile.append(card_to_play)
            print(f"{player} played: {card_to_play}")

            # Handle Wild and special card effects
            if card_to_play.get('special') == 'Wild':
                chosen_color = input("Choose a color (Red, Blue, Green, Yellow): ").capitalize()
                discard_pile[-1]['color'] = chosen_color
                print(f"{player} changed the color to {chosen_color}!")
            elif card_to_play.get('special') == 'Wild Draw Four':
                chosen_color = input("Choose a color (Red, Blue, Green, Yellow): ").capitalize()
                discard_pile[-1]['color'] = chosen_color
                print(f"{player} changed the color to {chosen_color}!")
                next_player = turn_order[1]
                drawn_cards, deck, discard_pile = draw_cards(deck, 4, discard_pile)
                players[next_player].extend(drawn_cards)
                print(f"{next_player} drew 4 cards: {drawn_cards}")

            # Handle other special cards
            elif card_to_play.get('special') == 'Skip':
                print("Next player's turn is skipped!")
                turn_order.append(turn_order.pop(0))  # Skip the next player
            elif card_to_play.get('special') == 'Reverse':
                print("Turn order is reversed!")
                turn_order.reverse()
            elif card_to_play.get('special') == 'Draw Two':
                print("Next player draws two cards!")
                next_player = turn_order[1]
                drawn_cards, deck, discard_pile = draw_cards(deck, 2, discard_pile)
                players[next_player].extend(drawn_cards)
                print(f"{next_player} drew: {drawn_cards}")
        else:
            print(f"{player} skipped their turn (invalid choice or skipped).")
    else:
        print("No valid cards to play. Drawing a card...")
        drawn_card, deck, discard_pile = draw_cards(deck, 1, discard_pile)
        players[player].append(drawn_card[0])
        print(f"{player} drew a card: {drawn_card[0]}")

    # Check for "UNO!"
    if len(players[player]) == 1:
        print(f"{player} has only one card left! UNO!")

    return players, deck, discard_pile, turn_order

if __name__ == "__main__":
    # Step 1: Create the deck
    deck = create_deck()
    print(f"Deck created with {len(deck)} cards.")
    print("Sample cards from the shuffled deck:", deck[:5])

    # Step 2: Initialize the game
    players, deck, discard_pile = initialize_game(deck)
    print("\nGame Initialized!")
    print("Player Hands:")
    for player, hand in players.items():
        print(f"{player}: {hand}")
    print(f"Discard Pile: {discard_pile}")
    print(f"Remaining cards in the deck: {len(deck)}")

    # Step 3: Play turns
    turn_order = ['Player 1', 'Player 2']
    while True:
        current_player = turn_order[0]
        players, deck, discard_pile, turn_order = play_turn(current_player, players, deck, discard_pile, turn_order)

        # Check for winner
        for player, hand in players.items():
            if not hand:
                print(f"{player} has won the game!")
                exit()

        # Rotate turn order
        turn_order.append(turn_order.pop(0))
