#Blackjack Program
import random
import os
import art
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card_generated=random.choice(cards)
    return card_generated

def calculate_score(cards):
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
  # and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, 
  # remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score,computer_score):
    if player_score==computer_score:
        return("Draw")
    elif computer_score==0:
        return("The DEALER wins")
    elif player_score==0:
        return("The PLAYER wins")
    elif player_score>21:
        return("Player score exceeded, the DEALER wins")
    elif computer_score>21:
        return("DEALER score exceeded, the PLAYER wins")
    elif player_score>computer_score:
        return("The PLAYER wins")
    else:
        return("The DEALER wins")
def main_game():
    print(art.logo)
    player_cards=[]
    computer_cards=[]
    game_over=False
    while game_over==False: #for player 
        for i in range(0,2):
            player_cards.append(deal_card())
            computer_cards.append(deal_card())

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Player cards: {player_cards} and the current score is: {player_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if player_score==0 or computer_score==0 or player_score>21:
            game_over=True
        else:
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. 
            # If yes, then use the deal_card() function to add another card to the user_cards List. 
            # If no, then the game has ended.
            user_should_deal=input("Types 'yes' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=="yes":
                player_cards.append(deal_card())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:   #for the computer to play.The computer needs to keep drawing cards 
        #as long as it has a score less than 17 and if the total of it is not 0, as 0 represents its a blackjack
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"PLAYER'S FINAL HAND: {player_cards}, the final score: {player_score}")
    print(f"DEALER'S FINAL HAND: {computer_cards}, the final score: {computer_score}")
    print(compare(player_score,computer_score))

    while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")=="yes":
        os.system('cls')
        main_game()
