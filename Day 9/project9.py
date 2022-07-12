import os
import art 
print(art.logo)
auction={} #initial empty dictionary in which all the records will be stored  having the key as the name of the bidder and the value as the bid by that person
choice=True 
def auction_winner(bidding_record):
    highest_bid=0 #initial bid_amount and this will be compared with each and every bidding amount entered by the user
    #bidding record is a dictionary having the key as the name of the bidder and the value as the bid by that person 
    for bidder in bidding_record: #bidder is the key of each element in the dictionary
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid amount of {highest_bid}")

while choice==True:
    name=input("Please enter your name: ")
    bid=int(input("Please enter your bid: "))
    auction[name]=bid 
    continue_choice=input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if continue_choice=="no":
        choice=False
        auction_winner(auction)
    elif continue_choice=="yes":
        os.system('cls')