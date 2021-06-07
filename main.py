import random
from art import logo
import os


def deal_card():
    """Returns a random playing card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def clear_screen():  # sometimes the clear_screen function does'nt functioning properly
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def cards_sum(player_cards):
    """Returns the summation of the cards"""
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)


def compare(user_score, computer_score):
    """compares computer's score with the user's score."""
    if computer_score == user_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose."
    elif user_score == 0:
        return "You win."
    elif user_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win."
    elif computer_score > user_score:
        return "You lose."
    else:
        return "You win."


def blackjack():
    """Blackjack game."""
    print(logo)
    print("\n")
    computer = []
    user = []
    is_game_over = False
    for _ in range(2):
        computer.append(deal_card())
        user.append(deal_card())
        computer_sum = cards_sum(computer)
    while not is_game_over:
        user_sum = cards_sum(user)
        print(f"Your cards {user}, current score: {user_sum}.")
        print(f"Computer's first card {computer[0]}.")
        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            is_game_over = True
        else:
            play = input("Type 'y' to get another card or type 'n'to pass: ").lower()
            if play == 'y':
                user.append(deal_card())
            else:
                is_game_over = True
    while computer_sum != 0 and computer_sum < 17:
        computer.append(deal_card())
        computer_sum = cards_sum(computer)
    print(f"Your final hand: {user}, final score: {user_sum}.")
    print(f"Computer's final hand: {computer}, final score: {computer_sum}.")
    print(compare(user_sum, computer_sum))
    print("\n")


while input("Do u want to play Blackjack? type 'y' or 'n': ").lower() == 'y':
    blackjack()
    clear_screen()
print("\nGood bye.")
