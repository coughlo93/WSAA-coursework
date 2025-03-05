import requests
import time

def shuffle_deck():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    data = response.json()
    return data["deck_id"]

def draw_cards(deck_id, count=5):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(url)
    data = response.json()
    return data["cards"]

def check_hand(cards):
    values = [card['value'] for card in cards]
    suits = [card['suit'] for card in cards]
    
    value_counts = {val: values.count(val) for val in set(values)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}
    
    if 4 in value_counts.values():
        print("Congratulations! You got Four of a Kind!")
    elif 3 in value_counts.values() and 2 in value_counts.values():
        print("Congratulations! You got a Full House!")
    elif 3 in value_counts.values():
        print("Congratulations! You got Three of a Kind!")
    elif list(value_counts.values()).count(2) == 2:
        print("Congratulations! You got Two Pairs!")
    elif 2 in value_counts.values():
        print("Congratulations! You got a Pair!")
    
    if len(suit_counts) == 1:
        print("Wow! You got a Flush! All cards are the same suit!")
    
    value_ranks = {"ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11,
                   "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
                   "4": 4, "3": 3, "2": 2}
    sorted_values = sorted([value_ranks[v] for v in values])
    
    if sorted_values == list(range(min(sorted_values), min(sorted_values) + 5)):
        print("Awesome! You got a Straight!")

def main():
    deck_id = shuffle_deck()
    print("Shuffling deck...")
    time.sleep(2)
    print(f"Deck shuffled. Deck ID: {deck_id}")
    
    print("Drawing 5 cards...")
    time.sleep(2)
    cards = draw_cards(deck_id)
    
    print("Your cards:")
    for card in cards:
        print(f"{card['value']} of {card['suit']}")
    
    check_hand(cards)
    
if __name__ == "__main__":
    main()