import os as system

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} by bidding {highest_bid}")

while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bidding amount: "))
    bids[name] = price
    should_continue = input("Is there any other bidder? Type 'yes' or 'no': ").lower()
    if should_continue == "yes":
        system.system("cls")   # use "clear" if you're on Linux/Mac
    else:
        bidding_finished = True
        find_highest_bidder(bids)

