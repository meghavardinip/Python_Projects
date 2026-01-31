import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_list=[]
computer_list=[]
def game_on():
    card_drawn= random.randrange(len(cards))
    player_pick=cards[card_drawn]
    return player_pick
def new_round():
    global player_list,computer_list
    player_list = [game_on(), game_on()]
    computer_list = [game_on(), game_on()]
    print(f"User's cards: {player_list}")
    print(f"Computer's first card is {computer_list[0]} ")
    total1 = sum(player_list)
    total2 = sum(computer_list)  # Only the first card is visible initially
    players_turn(total1, total2)
def play_again():
    again = input("Do you want to play another round? (y/n): ")
    if again == "y":
        print(art.logo)
        new_round()
    else:
        print("Game Over. Thanks for playing!")
def start_game():
    start_decision = input("Do you want to play a game of Blackjack? (y/n): ")
    if start_decision == 'y':
        print("Starting the game...")
        print(art.logo)
        new_round()
    else:
        print("Maybe next time! Game Over.")
def check_blackjack():
    if len(player_list) == 2 and 11 in player_list and 10 in player_list:
        return "User Wins"
    elif len(computer_list) == 2 and 11 in computer_list and 10 in computer_list:
        return "Computer Wins"
    return None

def check_ace():
    for card in player_list:
        if card== 11:
            return True
    return None
def who_wins(total1,total2):
    if total2 <= 21 and total1 <= 21:
        if total2 > total1:
            print(f"computer cards are {computer_list}")
            print(f"Computer's score is {total2}")
            print("Computer wins")
        elif total1 > total2:
            print(f"computer cards are {computer_list}")
            print(f"Computer's score is {total2}")
            print("player wins")
        elif total1 == total2:
            print(f"computer cards are {computer_list}")
            print(f"Computer's score is {total2}")
            print("Draw")
    elif total1 > 21:
        print(f"computer cards are {computer_list}")
        print(f"Computer's score is {total2}")
        print("Player loses")
    elif total2 > 21:
        print(f"computer cards are {computer_list}")
        print(f"Computer's score is {total2}")
        print("Computer loses")
    play_again()
def computer_turn(total2,total1):
    print(f"Computer's cards: {computer_list}")
    while total2<17:
        computer_list.append(game_on())
        total2 = sum(computer_list)
        print(f"Updated computer cards are {computer_list}")
    who_wins(total1,total2)
    return None

def continue_or_not():
    continue1 = input("Do you want to draw another card say y/n")
    return continue1
def players_turn(total1,total2):
    blackjack_result=check_blackjack()
    if blackjack_result:
        print(blackjack_result)
        print("Game over")
        play_again()
        return
    if total1>21 and check_ace():
        for i in range(len(player_list)):
            if player_list[i] == 11:
                player_list[i]=1
                total1=sum(player_list)
                break
    elif total1 > 21:
        print(f"The updated player's list is {player_list}")
        print(f"player's score is {total1}")
        print("Player loses")
        play_again()
        return

    elif total1==21:
        print("Player Wins")
        play_again()
        return
    elif total1<21:
        decision=continue_or_not()
        if decision=="y":
            player_list.append(game_on())
            total1=sum(player_list)
            print(f"Updated player cards: {player_list} (Total: {total1})")
            print(f"computer's cards are {computer_list}")
            print(f"Computer's score {total2}")
            players_turn(total1,total2)
        elif decision=="n":
            if total2<17:
                computer_turn(total2,total1)
            else:
                who_wins(total1,total2)
    return None
start_game()