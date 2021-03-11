from clear import clear
from art import logo
print(logo)
print("*Posh Butler accent*")

bids = {}
def bid_info():
    bidder_name = input("Bidder's name please:\n")
    bid_price = input("And the price.\n")
    bids[bidder_name] = int(bid_price)

bid_info()
restart_or_not = input("Are there any further bidders at this fine auction? Yes or No please 🙄\n")

while restart_or_not == "Yes":
    clear()
    bid_info()
    restart_or_not = input("Are there any further bidders at this fine auction? Yes or No please 🙄\n")

winning_bidder = max(bids)
winning_bid = bids[winning_bidder]

print(f"The winner of this eerily silent auction is {winning_bidder}.. with their bid of {winning_bid}!")
