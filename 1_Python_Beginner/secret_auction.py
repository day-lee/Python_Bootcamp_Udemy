
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def finding_winner(bidders_info):
    highest_bidder = 0
    winner = ''
    for key in bidders_info:
        bidder_price = bidders_info[key]
        if bidder_price > highest_bidder:
            highest_bidder = bidder_price
            winner = key
    print(logo)
    print(f"\n{winner} is a winner with a bid of ${highest_bidder}.")

auction_finished = False
bidder_dict = {}
while not auction_finished:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bidder_dict[name] = bid_amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' : ")
    if other_bidders == "yes":
        print(logo)
    elif other_bidders == "no":
        finding_winner(bidder_dict)
        auction_finished = True
