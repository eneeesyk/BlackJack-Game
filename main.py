import random

def choice_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw!"
    elif comp_score == 0:
        return "You lose! Computer has Blackjack!"
    elif user_score == 0:
        return "You win! With a Blackjack!"
    elif user_score > 21:
        return "You ran out of 21! You lose!"
    elif comp_score > 21:
        return "Computer has ran out of 21! You win!"
    elif user_score > comp_score:
        return "You win!"
    else:
        return "You lose"

def game():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(choice_card())
        computer_cards.append(choice_card())

    while not game_over:
        sum_of_user = score(user_cards)
        sum_of_comp = score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {sum_of_user}")
        print(f"    Computer first card: {computer_cards[0]}")

        if sum_of_user == 0 or sum_of_comp == 0 or sum_of_user > 21:
            game_over = True
        else:
            choice_for_user = input("Type 'yes' to get one more card, type 'no' for pass: ")
            if choice_for_user == 'yes':
                user_cards.append(choice_card())
            else:
                game_over = True

    while sum_of_comp != 0 and sum_of_comp < 17:
        computer_cards.append(choice_card())
        sum_of_comp = score(computer_cards)

    print(f"Your final hand is: {user_cards}, final score {sum_of_user}")
    print(f"Computer's final hand is: {computer_cards}, final score {sum_of_comp}")
    print(compare(sum_of_user, sum_of_comp))

while input("Do you want to play game? Type 'y' or 'n': ") == "y":
    game()
