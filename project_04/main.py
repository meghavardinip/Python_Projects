import art

bid_info = {}
def find_highest_bidder(bidding_dictionary):
    highest_bid=0
    winner=""
    for name in bidding_dictionary:
        bidful_bidder=bidding_dictionary[name]
        if bidful_bidder>highest_bid:
            highest_bid=bidful_bidder
            winner=name
    print(f"the winner of the bid is {winner} with bid {highest_bid}")
def bid_start():
    continue_bidding=True
    while continue_bidding:
        name=input("Enter bidder's name:")
        bid=int(input("What is your bid?$"))
        bid_info[name]=bid
        proceed_further=input("if there is another bidder?type if 'yes' or 'no':")
        if proceed_further=="no":
            find_highest_bidder(bid_info)
            continue_bidding=False
            bid_on()
        elif proceed_further=="yes":
            bid_start()
    return None
def bid_on():
    start=input("Welcome to the online bidding game, if you want to continue type y/n:")
    if start=="y":
        print(art.logo)
        bid_start()
    elif start=="n":
        print("Thankyou!")
        return
bid_on()
