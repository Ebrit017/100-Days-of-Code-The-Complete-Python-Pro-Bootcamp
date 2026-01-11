import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner_name = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            winner_name = bidder
            highest_bid = bid_amount
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

bids = {}
bidding = True

while bidding:
    name_input = str(input("What is your name?: "))
    bid_input = int(input("What is your bid? $"))

    bids[name_input] = bid_input

    more_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if more_bidders == "no":
        bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 100)