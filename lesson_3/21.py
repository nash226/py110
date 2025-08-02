"""
This is a blackjack style card game with simple rules: 21
"""
import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

def prompt(message):
    #Decorates our outputs
    print(f'=> {message}')

def initialize_deck():
    #creates a randomized deck
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)
    return deck

def total(cards):
    #calculate total for cards and account for aces being 1 or 11
    sum_val = 0
    for card in cards:
        value = card[:-1]

        if value == 'A':
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    for card in cards:
        value = card[:-1]
        if sum_val <= 21:
            break
        if value == 'A':
            sum_val -= 10
    return sum_val

def busted(cards):
    #lets us know that a player has lost
    return cards > 21

def detect_result(dealer_cards, player_cards):
    #logic for busting or winning
    player_total = player_cards
    dealer_total = dealer_cards

    if player_total > 21:
        return "PLAYER_BUSTED"
    elif dealer_total > 21:
        return "DEALER_BUSTED"
    elif dealer_total < player_total:
        return "PLAYER"
    elif dealer_total > player_total:
        return "DEALER"
    else:
        return "TIE"

def display_results(dealer_cards, player_cards):
    #prints out who won or if tie
    result = detect_result(dealer_cards, player_cards)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case 'TIE':
            prompt('Its a tie!')
    return result # I am returning result so I can calculate series score

def play_again():
    #asking to play again and handling for innapropriate output
    print('-----------------')
    answer = input('Do you want to play again? (y or n) ').strip().lower()
    while answer.lower() not in ['y', 'n']:
        answer = input('Please enter y or n: ')
    return answer.lower() == 'y'

def pop_two_from_deck(deck):
    #removing cards from deck
    return [deck.pop(), deck.pop()]

def hand(cards):
    #returns all the cards in the players hands
    return ', '.join(cards)

def grand_display(dealer_cards, d_total, player_cards, p_total):
    #gives a display of cards and total
    print('===============')
    prompt(f'Dealer has {hand(dealer_cards)}, for a total of: {d_total}')
    prompt(f'Player has {hand(player_cards)}, for a total of: {p_total}')
    print('===============')

def series_score(dealer, player):
    prompt(f'Dealer {dealer}: Player {player}')




while True:
    prompt('Welcome to 21!')
    prompt('You are playing best of 5 \n')

    player = 0
    dealer = 0

    while player < 3 and dealer < 3:
        #initial deal
        deck = initialize_deck()
        player_cards = pop_two_from_deck(deck)
        dealer_cards = pop_two_from_deck(deck)

        p_total = total(player_cards)
        d_total = total(dealer_cards)

        prompt(f"Dealer has {dealer_cards[0]} and ?")
        prompt(f"You have: {player_cards[0]} and {player_cards[1]},"
            f"for a total of {p_total}. ")

        #player turn
        while True:
            player_choice = input("Would you like to (h)it or (s)tay? ")
            if player_choice not in ['h', 's']:
                prompt("Sorry, must enter 'h' or 's'.")
                continue

            if player_choice == 'h':
                player_cards.append(deck.pop())
                prompt("You chose to hit!")
                prompt(f'Your cards are now {hand(player_cards)}')
                prompt(f'Your total is now: {total(player_cards)}')
                p_total = total(player_cards)
        
            if player_choice == 's' or busted(p_total):
                break
        if busted(p_total):
            grand_display(dealer_cards, d_total, player_cards, p_total)
            display_results(d_total, p_total)
            dealer += 1
            series_score(dealer, player)
            continue
        else:
            prompt(f'You stayed at {p_total}')

        #dealers turn
        prompt("Dealers turn...")

        while total(dealer_cards) < 17:
            prompt("Dealer hits!")
            dealer_cards.append(deck.pop())
            prompt(f"Dealer's cards are now: {hand(dealer_cards)}")
            d_total = total(dealer_cards)

        #updates score of player if dealer busts
        if busted(d_total):
            grand_display(dealer_cards, d_total, player_cards, p_total)
            display_results(d_total, p_total)
            player += 1
            series_score(dealer, player)
            continue
        else:
            prompt(f"Dealer stays at {d_total}")

        #both player and dealer stays
        grand_display(dealer_cards, d_total, player_cards, p_total)

        #calculates score based on who wins
        result = display_results(d_total, p_total)
        if result == 'PLAYER':
            player += 1
        if result == 'DEALER':
            dealer += 1
        series_score(dealer, player)

    
    prompt("Series over!")
    if player == 3:
        prompt("Player wins the match!")
    else:
        prompt("Dealer won the match!")

    if not play_again():
        break
    



